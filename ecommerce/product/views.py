from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# from django.views.generic import DetailView
# from analytics.mixins import ObjectViewedMixin
# from cart.models import Cart

# Create your views here.

def product_detail(request, slug):
    product_detail = get_object_or_404(Product, slug=slug)
    context = {
        "product_detail":product_detail
    }
    return render(request, 'product_detail.html', context)

