from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     #login
     path('login',views.MyTokenObtainPairView.as_view()),
     
     path('',views.index),
     #singup
     path('register',views.register),
     
     
     #test login 
     path('members',views.test_members),
     path('buy_car',views.buy_car), 
     path('get_my_cars',views.get_my_cars), 
     path('get_my_cars/<id>',views.get_my_cars), 


]
