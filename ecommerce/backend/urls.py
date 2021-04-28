from .views import *
from django.urls import path
from backend.views import LoginTokenView,RegisterViews

urlpatterns=[
    path("api/user/", UserDetail.as_view()),
    path('api/login/',LoginTokenView.as_view()),
    path('api/register/',RegisterViews.as_view()),
]