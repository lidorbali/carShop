from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('login',views.MyTokenObtainPairView.as_view()),
     path('register',views.register),
     path('members',views.test_members),
     path('buy_car',views.buy_car), 
     path('get_my_cars',views.get_my_cars), 


]
