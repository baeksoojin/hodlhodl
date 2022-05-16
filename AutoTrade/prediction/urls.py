from django.urls import path
import prediction.views as views

app_name = 'prediction'

urlpatterns = [
    path('linechart/',views.prediction_linechart,name='prediction_linechart'),
]