from django.shortcuts import redirect, render
from Sentiment.models import Sentiment, Comments
from django.forms.models import model_to_dict
import json

# Create your views here.
def sentiment_piechart(request):
    
    sentiment = Sentiment.objects.last() #가장 최신값을 불러와서 보여줌
    print(sentiment)
    res_data = model_to_dict(sentiment)
    print(res_data)
    
    # datetime 객체 string으로 변환
    res_data['crawling_date'] = res_data['crawling_date'].strftime("%Y %b %d")
    print(res_data['crawling_date'])
    res_data=json.dumps(res_data)

    return render(request,"AI_result/piechart.html",{'res_data' : res_data})