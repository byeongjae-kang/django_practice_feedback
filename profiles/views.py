from django.views import View
from django.shortcuts import render

# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")
