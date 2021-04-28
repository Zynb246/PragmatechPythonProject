from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from backend.models import User
from .serializers import TokenPairSerializers, RegisterSerializers
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from rest_framework import generics

class LoginTokenView(TokenObtainPairView):
    serializer_class = TokenPairSerializers

class RegisterViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

# Create your views here.
class UserDetail(APIView):
    def get(self,request):
        print(self.request.user)
        user=User.objects.filter(id=self.request.user.id)
        print(user)
        serializer=UserSerializers(user,many=True)
        return Response(serializer.data)