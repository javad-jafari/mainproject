from django.utils import timezone

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SlideShow
from Products.models import Category, Product


# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slides"] = SlideShow.objects.all()
        context["categories"] = Category.objects.all()
        context["product"] = Product.objects.all()
        context["time"] = timezone.now()
        return context
