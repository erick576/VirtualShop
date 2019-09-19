from django.urls import path
from . import views


# /items

urlpatterns = [
    path('', views.index),
]
