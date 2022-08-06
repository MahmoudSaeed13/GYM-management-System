from django.urls import path
from classes import views

urlpatterns = [
    path('', views.index, name='index'),
]
