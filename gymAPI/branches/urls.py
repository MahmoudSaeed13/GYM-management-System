from django.urls import path
from branches import views

urlpatterns = [
    path('', views.index, name='index'),
]