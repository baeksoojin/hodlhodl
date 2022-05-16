from django.urls import path,include
import Sentiment.views as views

app_name = 'Sentiment'

urlpatterns = [
    path('piechart/',views.sentiment_piechart,name='sentiment_piechart'),
]