import time
import pyupbit
import datetime
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
import environ
import os
import json

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

env = environ.Env()
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

access = env('access')
secret = env('secret')

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

ticker = "KRW-BTC" #장고에서 사용자가 선택할 수 있도록.
days = 7 #day기준 # 7일치를 보여줄예정.

context = {} #장고 function 안에 사용해서 html에 rendering할 예정

def get_ohlc_context(ticker,days):

    df = pyupbit.get_ohlcv(ticker, interval="day", count=days)
    #0부터 과거의 값이 저장됨.
    print(df) #index값이 9시기준으로 나눠지는 날짜로 알 수 있음.
    print(df.columns) #'open', 'high', 'low', 'close', 'volume', 'value' 등이 존재함을 알 수 있음. 
    print(df.index[0]) # 0값이 가장 이전의 (가장 과거의 데이터) 데이터임을 알 수 있음
    
    context = {}

    context["open"]=[]
    context["close"]=[]
    context["high"]=[]
    context["low"]=[]
    context["date"]=[]

    for i in range(0,7):

        open = df.iloc[i][0]
        high = df.iloc[i][1]
        low = df.iloc[i][2]
        close = df.iloc[i][3]
        date = str(df.index[i])
        date = date[5:10]

        context["open"].append(open)
        context["close"].append(close)
        context["high"].append(high)
        context["low"].append(low)
        context["date"].append(date)

    print(context)
    
    # context = json.dumps(context)
    # print(context)
    #장고에서 넘길때는 return render(request, 'AutoTrading.html', {'context': context}) 으로 사용
    return context

get_ohlc_context(ticker,days)
