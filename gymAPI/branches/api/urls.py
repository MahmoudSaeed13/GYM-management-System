from branches.api.views import BranchesList, BranchCreate, BranchDelete, BranchUpdate, BranchView
from django.urls import path



urlpatterns = [
    path('', BranchesList.as_view()),
    path('create/', BranchCreate.as_view()),
    path('class/<int:pk>', BranchView.as_view()),
    path('class/<int:pk>/update', BranchUpdate.as_view()),
    path('class/<int:pk>/delete', BranchDelete.as_view()),
]