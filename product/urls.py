from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index,name="index"),
    path('register', views.register,name="index"),
    path('logout', views.logout,name="logout"),
    path('login', views.login,name="loging"),
    path('check', views.check,name="check"),
]
