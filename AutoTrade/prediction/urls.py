from django.urls import path
import prediction.views as views

app_name = 'prediction'

urlpatterns = [
    path('result/',views.prediction_result,name='prediction_result'),
]