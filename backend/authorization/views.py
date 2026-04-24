from django.shortcuts import render
from django.contrib.auth import get_user_model #37
from rest_framework.views import APIView #38
from rest_framework.response import Response #39
from .serializers import UserSerializer #40
from rest_framework.permissions import AllowAny #41
from rest_framework import status #42
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
# Create your views here.

User = get_user_model()

class RegisterView(APIView): #43 -> backend/urls.py
    permission_classes = [AllowAny]

    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)