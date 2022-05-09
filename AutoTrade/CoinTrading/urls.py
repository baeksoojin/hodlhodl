from django.urls import path,include
import CoinTrading.views as views

app_name = 'CoinTrading'

urlpatterns = [
    path('situation/',views.Situation,name='situation'),
]