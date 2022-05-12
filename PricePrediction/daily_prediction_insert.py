import time
import pyupbit
import datetime
import pandas as pd
import numpy as np
import warnings
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv1D, Lambda
from tensorflow.keras.losses import Huber
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import pymysql 


def predict_start():
    access = "key"
    secret = "key"

    upbit = pyupbit.Upbit(access, secret)

    ticker = "KRW-BTC"
    df = pyupbit.get_ohlcv(ticker, interval="day", count=3650)

    df_org = df.copy()

    # stationary -> non-stationary
    df["open_diff"] = df["open"] - df["open"].shift(1)
    df["high_diff"] = df["high"] - df["high"].shift(1)
    df["low_diff"] = df["low"] - df["low"].shift(1)
    df["close_diff"] = df["close"] - df["close"].shift(1)

    df2 = df[["open_diff", "high_diff", "low_diff", "close_diff", "volume", "close"]]

    # smoothing by MA
    df2["close_diff_ma5"] = df2["close_diff"].rolling(window=5).mean()
    df2["close_diff_ma10"] = df2["close_diff"].rolling(window=10).mean()
    df2["close_diff_ma20"] = df2["close_diff"].rolling(window=20).mean()
    df2["close_diff_ma60"] = df2["close_diff"].rolling(window=60).mean()
    df2["close_diff_ma120"] = df2["close_diff"].rolling(window=120).mean()

    df = df2[["close_diff_ma5", "close_diff_ma10", "close_diff_ma20", "close_diff_ma60", "close_diff_ma120", "close"]]

    df = df.dropna()
    df_drop = df

    warnings.filterwarnings('ignore')

    # inverse transform
    def restore(row):
    return row * (max(df_drop["close"]) - min(df_drop["close"])) + min(df_drop["close"])


    scaler = MinMaxScaler()
    # 스케일을 적용할 column을 정의합니다.
    scale_cols = ["close_diff_ma5", "close_diff_ma10", "close_diff_ma20", "close_diff_ma60", "close_diff_ma120", "close"]
    # 스케일 후 columns
    scaled = scaler.fit_transform(df[scale_cols])

    df = pd.DataFrame(scaled, columns=scale_cols)

    x_train, x_test, y_train, y_test = train_test_split(df.drop('close', 1), df['close'], test_size=0.2, random_state=0, shuffle=False)

    df2 = df_org

    def windowed_dataset(series, window_size, batch_size, shuffle):
        series = tf.expand_dims(series, axis=-1)
        ds = tf.data.Dataset.from_tensor_slices(series)
        ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
        ds = ds.flat_map(lambda w: w.batch(window_size + 1))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.map(lambda w: (w[:-1], w[-1]))
        return ds.batch(batch_size).prefetch(1)

    WINDOW_SIZE=20
    BATCH_SIZE=32

    # trian_data는 학습용 데이터셋, test_data는 검증용 데이터셋 입니다.
    train_data = windowed_dataset(y_train, WINDOW_SIZE, BATCH_SIZE, True)
    test_data = windowed_dataset(y_test, WINDOW_SIZE, BATCH_SIZE, False)

    # 아래의 코드로 데이터셋의 구성을 확인해 볼 수 있습니다.
    # X: (batch_size, window_size, feature)
    # Y: (batch_size, feature)
    for data in train_data.take(1):
        print(f'데이터셋(X) 구성(batch_size, window_size, feature갯수): {data[0].shape}')
        print(f'데이터셋(Y) 구성(batch_size, window_size, feature갯수): {data[1].shape}')

    model = Sequential([
        # 1차원 feature map 생성
        Conv1D(filters=32, kernel_size=5,
            padding="causal",
            activation="relu",
            input_shape=[WINDOW_SIZE, 1]),
        # LSTM
        LSTM(16, activation='tanh'),
        Dense(16, activation="relu"),
        Dense(1),
    ])

    # Sequence 학습에 비교적 좋은 퍼포먼스를 내는 Huber()를 사용합니다.
    loss = Huber()
    optimizer = Adam(0.0005)
    model.compile(loss=Huber(), optimizer=optimizer, metrics=['mse'])

    # earlystopping은 10번 epoch통안 val_loss 개선이 없다면 학습을 멈춥니다.
    earlystopping = EarlyStopping(monitor='val_loss', patience=10)
    # val_loss 기준 체크포인터도 생성합니다.
    filename = os.path.join('tmp', 'ckeckpointer.ckpt')
    checkpoint = ModelCheckpoint(filename, 
                                save_weights_only=True, 
                                save_best_only=True, 
                                monitor='val_loss', 
                                verbose=1)

    history = model.fit(train_data, 
                        validation_data=(test_data), 
                        epochs=50, 
                        callbacks=[checkpoint, earlystopping])

    model.load_weights(filename)

    pred = model.predict(test_data)

    df_actu = df_org[-len(pred):]

    df_actu["pred"] = restore(pred)
    df_actu = df_actu[["close", "pred"]]

    prediction_data = df_actu


    # date값이 Unnamed: 0 으로 되어있으니까 수정후 작업 진행.
    prediction_data.rename(columns = {'Unnamed: 0' : 'date'}, inplace = True)

    # lstm을 활용한 prediction값 모두 저장.

    conn = pymysql.connect(host='autotrading-db.cjolqhecq70a.ap-northeast-2.rds.amazonaws.com',
                        user = 'admin',
                        password='key',
                        db = 'AutoTrading',
                        charset = 'utf8')
    curs = conn.cursor()


    #시간은 9시 고정이니까 없애고 날짜 date값만 남기기 위해서 pandas 사용
    prediction_data['date'] = pd.to_datetime(prediction_data['date']).dt.date


    sql_row = [(prediction_data['date'][-1],prediction_data['pred'][-1])]


    insert_result = """insert into prediction(prediction_date,pred_price) values (%s, %s, %s)"""
    curs.executemany(insert_result,sql_rows)
    conn.commit()
    conn.close()

schedule.every().day.at("09:01").do(lambda: predict_start())