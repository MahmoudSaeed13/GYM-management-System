from trainers.api.views import *
from django.urls import path

urlpatterns = [
    path('', TrainersListView.as_view(), name="list-trainers"),
    path('create/', TrainerCreateView.as_view(), name="add-trainer"),
    path('detail/<int:pk>/', TrainerDetailView.as_view(), name="trainer-details"),
    path('update/<int:pk>/', TrainerUpdateView.as_view(), name="update-trianer"),
    path('delete/<int:pk>/', TrainerDeleteView.as_view(), name="delete-trainer"),
]