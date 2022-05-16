from django.shortcuts import render,redirect
from CoinTrading.candlechart import get_ohlc_context
import json

# Create your views here.
def Situation(request):

    context = get_ohlc_context("KRW-BCH",7)
    print("context :", context)
    print(type(context))
    res_data = json.dumps(context)

    return render(request,'CoinTrading/inner.html',{'res_data' : res_data})

