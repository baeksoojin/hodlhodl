from django.urls import path,include
import main.views as views


app_name = 'Home'

urlpatterns = [
    path('',views.index,name='main'),
    path('detail',views.detail,name='detail')
]