from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('sec/',views.sec, name="sec"),
    path('login/',views.signin, name="login"),
    path('register/',views.register, name="register"),
    path('logout/',views.Logout,name="Logout"),
]
