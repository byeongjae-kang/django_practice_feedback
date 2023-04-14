from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .form import ReviewForm
from .models import Review


# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for your review!!"

        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        print(loaded_review.id, request, favorite_id)
        context["is_favorite"] = favorite_id == str(loaded_review.id)

        return context


class FavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        print(request.session["favorite_review"])

        return HttpResponseRedirect("/reviews/" + review_id)
