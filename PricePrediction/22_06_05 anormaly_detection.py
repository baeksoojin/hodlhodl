import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
import yfinance as yf
import schedule
import pymysql

def detect_start():

    # Load the data
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    interval = "5m"
    # 9일부터 12일 폭락함
    start = "2022-04-29"
    end = "2022-05-13"
    df = yf.download("BTC-USD", start=start, end=end, interval=interval)
    df["close_chg"] = (df["Close"] - df["Close"].shift(1)) / df["Close"].shift(1) * 100
    btc = df[["close_chg"]]
    btc = btc.fillna(method = "bfill")


    # Prepare training data
    df_small_noise = btc # 정상
    # Normalize and save the mean and std we get,
    # for normalizing test data.
    training_mean = df_small_noise.mean()
    training_std = df_small_noise.std()
    df_training_value = (df_small_noise - training_mean) / training_std


    # Create sequences
    TIME_STEPS = 288

    # Generated training sequences for use in the model.
    def create_sequences(values, time_steps=TIME_STEPS):
        output = []
        for i in range(len(values) - time_steps + 1):
            output.append(values[i : (i + time_steps)])
        return np.stack(output)

    x_train = create_sequences(df_training_value.values)


    # Build a model
    model = keras.Sequential(
        [
            layers.Input(shape=(x_train.shape[1], x_train.shape[2])),
            layers.Conv1D(
                filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Dropout(rate=0.2),
            layers.Conv1D(
                filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Conv1DTranspose(
                filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Dropout(rate=0.2),
            layers.Conv1DTranspose(
                filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Conv1DTranspose(filters=1, kernel_size=7, padding="same"),
        ]
    )
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss="mse")


    # Train the model
    history = model.fit(
        x_train,
        x_train,
        epochs=50,
        batch_size=128,
        validation_split=0.1,
        callbacks=[
            keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, mode="min")
        ],
    )


    # Get train MAE loss.
    x_train_pred = model.predict(x_train)
    train_mae_loss = np.mean(np.abs(x_train_pred - x_train), axis=1)

    # Get reconstruction loss threshold.
    threshold = np.max(train_mae_loss)


    # Prepare test data 
    ticker = "BTC-USD"
    stock_data = yf.Ticker(ticker)
    hist="1mo"
    hist_data = stock_data.history(hist, interval="5m", auto_adjust=True)

    df = hist_data[["Close"]]
    df = df[-4032:]
    df["close_chg"] = (df["Close"] - df["Close"].shift(1)) / df["Close"].shift(1) * 100
    btc_curr = df[["close_chg"]]
    btc_curr = btc_curr.fillna(method = "bfill")
    df_daily_jumpsup = btc_curr


    # Normalizatoin 
    df_test_value = (df_daily_jumpsup - training_mean) / training_std

    # Create sequences from test values.
    x_test = create_sequences(df_test_value.values)

    # Get test MAE loss.
    x_test_pred = model.predict(x_test)
    test_mae_loss = np.mean(np.abs(x_test_pred - x_test), axis=1)
    test_mae_loss = test_mae_loss.reshape((-1))

    # Detect all the samples which are anomalies.
    anomalies = test_mae_loss > threshold


    # data i is an anomaly if samples [(i - timesteps + 1) to (i)] are anomalies
    anomalous_data_indices = []
    for data_idx in range(TIME_STEPS - 1, len(df_test_value) - TIME_STEPS + 1):
        if np.all(anomalies[data_idx - TIME_STEPS + 1 : data_idx]):
            anomalous_data_indices.append(data_idx)


    if anomalous_data_indices:
        print("anormaly detected!")
    else:
        print("normal state")

    print("sql insertion start")
    conn = pymysql.connect(host='autotrading-db.cjolqhecq70a.ap-northeast-2.rds.amazonaws.com',
                    user = 'admin',
                    password='key',
                    db = 'AutoTrading',
                    charset = 'utf8')
    curs = conn.cursor()

    df_daily_jumpsup = df_daily_jumpsup.reset_index()
    # df_daily_jumpsup['Datetime'] = pd.to_datetime(df_daily_jumpsup['Datetime']).dt.date

    sql_rows = []
    for i in range(len(df_daily_jumpsup)):
        sql_row = (df_daily_jumpsup['Datetime'][i], df_daily_jumpsup['close_chg'][i])
        sql_rows.append(sql_row)


    insert_result = "delete from detect"
    curs.execute(insert_result)

    insert_result = "insert into detect(prediction_date, close_chg) values (%s, %s)"
    curs.executemany(insert_result, sql_rows)

    conn.commit()
    conn.close()

    print("sql insertion completed")

schedule.every(5).minutes.do(lambda: detect_start())

while True:
    schedule.run_pending()