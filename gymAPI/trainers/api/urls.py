from trainers.api.views import *
# from rest_framework.routers import DefaultRouter
from django.urls import path



urlpatterns = [
    path('', TrainersListView.as_view()),
    path('create/', TrainerCreate.as_view()),
    path('trainer/<int:pk>', TrainerView.as_view()),
    path('trainer/<int:pk>/update', TrainerUpdate.as_view()),
    path('trainer/<int:pk>/delete', TrainerDelete.as_view()),
]