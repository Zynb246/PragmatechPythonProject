from django.urls import path
from .views import *

urlpatterns = [
   # path('<c_slug>/<subcat_slug>/<brand_slug>', subcategory_brands, name='subcategory_brands'),
    path('category/subcategory/brands/<brand_slug>', products_brand, name='products_brand'),
    # path('<cat_slug>/<subcat_slug>/<brand_slug>/<product_slug>', brand_products, name='brand_products'),

