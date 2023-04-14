from django.urls import path
from . import views

urlpatterns = [
    path("profiles", views.CreateProfileView.as_view()),
    path("list", views.UserProfileView.as_view()),
]
