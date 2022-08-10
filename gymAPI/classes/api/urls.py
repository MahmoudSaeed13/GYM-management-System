from classes.api.views import *
# from rest_framework.routers import DefaultRouter
from django.urls import path



urlpatterns = [
    path('', ClassesList.as_view()),
    path('create/', ClassCreate.as_view()),
    path('class/<int:pk>', ClassView.as_view()),
    path('class/<int:pk>/update', ClassUpdate.as_view()),
    path('class/<int:pk>/delete', ClassDelete.as_view()),
]