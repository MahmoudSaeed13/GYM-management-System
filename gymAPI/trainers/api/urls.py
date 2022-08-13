from trainers.api.views import *
from django.urls import path

urlpatterns = [
    path('', TrainersListView.as_view()),
    path('create/', TrainerCreateView.as_view()),
    path('detail/<int:pk>/', TrainerDetailView.as_view()),
    path('update/<int:pk>/', TrainerUpdateView.as_view()),
    path('delete/<int:pk>/', TrainerDeleteView.as_view()),
]