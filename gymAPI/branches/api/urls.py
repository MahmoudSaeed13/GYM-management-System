from branches.api import views
from django.urls import path



urlpatterns = [
    path('', views.BranchesListView.as_view(), name='branch-list'),
    path('create/', views.BranchCreateView.as_view(), name="branch-create"),
    path('class/<int:pk>', views.BranchDetailView.as_view(), name="branch-detail"),
    path('class/<int:pk>/update', views.BranchUpdateView.as_view(), name="branch-update"),
    path('class/<int:pk>/delete', views.BranchDelete.as_view(), name="branch-delete"),
]