from django.shortcuts import render
from .models import *

# Create your views here.
def products_brand(request,slug):
    product = Brand.products_in_brand( brand_slug=slug)

    context = {
        'brand':product
    }
    return render(request, 'product_brand.html', context)

