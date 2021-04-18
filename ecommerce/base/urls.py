from django.urls import path
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'model', ModelORder, basename='model')

urlpatterns = [
    
    path('api/v1/', include (router.urls)),
    path('', index, name='index'),
    path('api/product',ProductViews.as_view()),
    path('api/product/<id>/',ProductDetailViews.as_view()),
    path('add_to_wishlist/<int:id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_wishlist/', remove_wishlist, name='remove_wishlist')
]