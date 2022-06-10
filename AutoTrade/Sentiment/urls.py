from django.urls import path,include
import Sentiment.views as views

app_name = 'Sentiment'

urlpatterns = [
    path('result/',views.sentiment_result,name='sentiment_result'),

]