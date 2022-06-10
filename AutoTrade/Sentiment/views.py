from re import S
from django.shortcuts import redirect, render
from Sentiment.models import Sentiment, Comments, WordcloudTable
from django.forms.models import model_to_dict
from django.core import serializers
import json

# Create your views here.
def sentiment_result(request):
    
    sentiment = Sentiment

    sentiment = sentiment.objects.last()
    res_data = model_to_dict(sentiment)
    print(res_data)
    res_data['crawling_date'] = res_data['crawling_date'].strftime("%Y %b %d")
    res_data1 = json.dumps(res_data)
    
    # 각 단어의 언급량을 weight로 설정하여 워드 클라우딩을 진행한다.

    wordcloud = WordcloudTable.objects.last()
    print(wordcloud)
    temp = model_to_dict(wordcloud)
    print(temp)
    date = temp['crawling_date']
    print(date)

    wordcloud = WordcloudTable.objects.filter(crawling_date = date)
    print(wordcloud)
    
    res_data2=serializers.serialize("json",wordcloud)


    return render(request,"AI_result/sentiment.html",{ 'res_data1' : res_data1,'res_data2' : res_data2})
