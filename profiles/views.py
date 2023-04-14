from django.views import View
from django.views.generic import CreateView, ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import ProfileForm
from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "profiles"


class UserProfileView(ListView):
    template_name = "profiles/user_profile.html"
    model = UserProfile
    context_object_name = "profiles"
