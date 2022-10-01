from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from requests import Request
from accounts import serializers

from accounts.serializers import UserRegister
from accounts.models import Account
from .models import Ride, RideRequest
from cab.serializers import RideSerializer, RideRequestSerializer, GetRiderInfo, UserInfoSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import mixins, status, viewsets, generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import api_view, permission_classes

class Ride_Create(APIView):

    def post(self, request):
        user = Account.objects.get(id = request.user.id)

        create_ride =  RideSerializer(data=request.data)
        if create_ride.is_valid():
            create_ride.save(user = user)
            return Response(data = create_ride.data)
        else:
            data = create_ride.errors
            return Response(data = data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_rides(request):

    print('inside get_rides_funtion')
    print('data is hereeeeeeeeee', request.data)

    get_list = Ride.objects.filter(source_city=request.data['source_city'], destination_city=request.data['destination_city'], date=request.data['date'])

    serializer_class = GetRiderInfo(get_list, many=True)

    return Response(serializer_class.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_rie_request(request, user_id):
    from_user = request.user
    id_ride = request.data['id_ride']
    ride_id  = Ride.objects.get(id=id_ride)
    to_user = Account.objects.get(id=user_id)

    ride_request = RideRequest.objects.create(from_user=from_user,to_user=to_user,ride_id=ride_id)

    print('heree is ride request ',ride_request)
    if ride_request:
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

