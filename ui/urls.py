from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('getuser', views.getuser, name='getuser')
        ]
