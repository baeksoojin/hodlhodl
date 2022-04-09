from django.urls import path,include
import Account.views as views

app_name = 'Account'

urlpatterns = [
    path('signup/',views.Signup,name='Signup'),
    path('login/',views.Login,name='Login'),
    path('logout/',views.Logout,name='Logout'),
]