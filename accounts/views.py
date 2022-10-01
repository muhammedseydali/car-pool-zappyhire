from django.shortcuts import render
from .models import Account
from django.db import transaction
from .serializers import UserRegister, UserDataSerializer

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins, status, viewsets, generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView

# Create your views here.

class RegistersViews(generics.CreateAPIView):

    serializer_class = UserRegister
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "data": UserRegister(user,context=self.get_serializer_context()).data,
            "message": "Registered Successfully.  Now perform Login to get your token",
        })



class UsersLists(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        user = Account.objects.all()
        serializer = UserDataSerializer(user,many=True)
        return Response(serializer.data)
