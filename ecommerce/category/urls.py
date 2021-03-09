from django.urls import path
from .views import *

urlpatterns = [
    path('', category, name='category'),
    path('<c_slug>/', category_subcategories, name='category_subcategories'),
    path('<c_slug>/<subcat_slug>', subcategory_brands, name='subcategory_brands'),
]
