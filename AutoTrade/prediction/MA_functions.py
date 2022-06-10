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

#비트코인
ticker = "KRW-BTC" 

def get_ma5(ticker,df):
    """5일 이동 평균선 조회"""
    ma5 = df['close'].rolling(5).mean()
    df['ma5']=ma5
    return ma5

def get_ma20(ticker,df):
    """20일 이동 평균선 조회"""
    ma20 = df['close'].rolling(20).mean()
    df['ma20']=ma20
    return ma20

def get_ma60(ticker,df):
    """60일 이동 평균선 조회"""
    ma60 = df['close'].rolling(60).mean()
    df['ma60'] = ma60
    return  ma60

def get_ma120(ticker,df):
    """120일 이동 평균선 조회"""
    ma120 = df['close'].rolling(120).mean()
    df['ma120'] = ma120
    return  ma120


def get_MA(ticker,days):

    df = pyupbit.get_ohlcv(ticker, interval="day", count=days)
    get_ma5(ticker,df)
    get_ma20(ticker,df)
    get_ma60(ticker,df)
    get_ma120(ticker,df)
    
    return df
