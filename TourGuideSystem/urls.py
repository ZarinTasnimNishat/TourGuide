from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('SignUp', views.signup, name="SignUp"),
    path('SignIn', views.signin, name="SignIn"),
    path('SignOut', views.signout, name="SignOut")

]
