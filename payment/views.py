from django.shortcuts import render
from accounts.models import Account
from .models import Payments


from asyncio import start_unix_server
from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from requests import Request
from accounts import serializers

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import mixins, status, viewsets, generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


def Payment(request):

    payment_deatails = request.data['details']

    user = Account.objects.get(id=request.user.id)
    name = payment_deatails['payer']
    payer = payment_deatails['purchase_unit']

    full_name = str(name["name"]['given_name'])
    price = request.data['price']

    Payment.objects.create(payer=payer, full_name=full_name, price=price, status=True)

    return Response(status=status.HTTP_200_OK)