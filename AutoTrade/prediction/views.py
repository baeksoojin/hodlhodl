from django.shortcuts import redirect, render
from prediction.models import Prediction
from django.core import serializers
from django.forms.models import model_to_dict
import json


# Create your views here.
def prediction_result(request):

    predictions = Prediction.objects.all().order_by('id')
    res_data=[]
    for prediction in predictions:
        data = model_to_dict(prediction)
        data['prediction_date'] = data['prediction_date'].strftime("%Y %b %d")
        res_data.append(data)

    res_data=json.dumps(res_data)

    return render(request,"AI_result/prediction.html",{'res_data' : res_data})