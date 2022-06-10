from django.shortcuts import redirect, render
from prediction.models import Prediction
from django.core import serializers
from django.forms.models import model_to_dict
import json
from prediction.MA_functions import get_MA

# Create your views here.
# def prediction_result(request):

#     predictions = Prediction.objects.all().order_by('id')
#     res_data=[]
#     for prediction in predictions:
#         data = model_to_dict(prediction)
#         data['prediction_date'] = data['prediction_date'].strftime("%Y %b %d")
#         res_data.append(data)

#     res_data=json.dumps(res_data)
#     print(res_data)

#     return render(request,"AI_result/prediction.html",{'res_data' : res_data})


def prediction_result(request):

    predictions = Prediction.objects.all().order_by('id')

    #moving_average적용
    df = get_MA("KRW-BTC",len(predictions))
    print(len(predictions))

    res_data=[]
    for prediction in predictions:
        data = model_to_dict(prediction)
        data['prediction_date'] = data['prediction_date'].strftime("%Y %b %d")
        data['ma5'] = df['ma5'][data['id']-1]
        data['ma20'] = df['ma20'][data['id']-1]
        data['ma60'] = df['ma60'][data['id']-1]
        data['ma120'] = df['ma120'][data['id']-1]
        res_data.append(data)

    res_data=json.dumps(res_data)
    
    #json data에 NaN값이 있을 경우, 에러발생 => null로 변경
    if "NaN" in res_data:
        print("error : Unexpected token N in JSON at position 105 at JSON.parse (<anonymous>)")
    res_data = res_data.replace("NaN","null")
    print(type(res_data))
    print(res_data)
    
    return render(request,"AI_result/prediction.html",{'res_data' : res_data})