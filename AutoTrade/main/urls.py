from django.urls import path,include
import main.views as views

urlpatterns = [
    path('',views.index,name='main'),
    path('detail',views.detail,name='detail')
]