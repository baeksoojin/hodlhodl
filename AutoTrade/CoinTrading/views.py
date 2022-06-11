from django.shortcuts import render,redirect
from CoinTrading.candlechart import get_ohlc_context
from django.forms.models import model_to_dict
from django.core import serializers
import json
from .models import Detect, Result
from Sentiment.models import Sentiment
from django.core.paginator import Paginator

# Create your views here.
def Situation(request):

    context,context2 = get_ohlc_context("KRW-BCH",7)
    # print("context :", context)
    # print(type(context))
    res_data = json.dumps(context)

    
    res_data2=serializers.serialize("json", Detect.objects.all())
    # print(res_data2)

    return render(request,'CoinTrading/inner.html',{'res_data' : res_data, 'res_data2':res_data2})

def result(request):
    
    res_data=serializers.serialize("json", Result.objects.all())
    
    context = get_ohlc_context("KRW-BCH",20)
    res_data2 = json.dumps(context)

    res_data3 = serializers.serialize("json", Sentiment.objects.all())

    
    
    return render(request,'CoinTrading/result.html',{'res_data' : res_data,'res_data2' : res_data2,'res_data3' : res_data3})

def buy_sell(request):
    
    result_data = Result.objects.all()
    list_ = {}
    list_["result_data"] = result_data[:10]

    all_result_board = Result.objects.all().order_by("-result_date")
    list_["print_list"] = all_result_board
    page = int(request.GET.get("p", 1))
    pagenator = Paginator(all_result_board, 10)
    list_["result_board"] = pagenator.get_page(page)

    return render(request,'CoinTrading/result_buy_sell.html',list_)