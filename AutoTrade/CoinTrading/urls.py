from django.urls import path,include
import CoinTrading.views as views

app_name = 'CoinTrading'

urlpatterns = [
    path('situation/',views.Situation,name='situation'),
    path('result/',views.result,name='result'),
    path('buy_sell/',views.buy_sell,name='buy_sell'),
]