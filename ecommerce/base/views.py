from django.shortcuts import render
from category.models import Category
from Staticpage.models import Slider

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    slider = Slider.objects.all()

    context = {
        'slider':slider,
        'categories':categories,
    }

    return render(request,'index.html',context)


    