from branches.api import views
from django.urls import path


urlpatterns = [
    path('', views.BranchesListView.as_view(), name='branch-list'),
    path('create/', views.BranchCreateView.as_view(), name="branch-create"),
    path('<int:pk>/', views.BranchDetailView.as_view(), name="branch-detail"),
    path('update/<int:pk>/', views.BranchUpdateView.as_view(), name="branch-update"),
    path('delete/<int:pk>/', views.BranchDeleteView.as_view(), name="branch-delete"),
    path("add-class/", views.BranchClassCreateView.as_view(), name="add-branch-class"),
    path("delete-class/<int:pk>/", views.BranchClassDeleteView.as_view(), name="delete-branch-class"),
    path("classes/<int:pk>/", views.BranchClassListView.as_view(), name="branch-classes_list")
]