from accounts.models import Account
from operator import attrgetter
from .models import Ride, RideRequest, Copassenger
from django.db import transaction
from rest_framework import fields, serializers
    

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        exclude = ['user']

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'  


class GetRiderInfo(serializers.ModelSerializer):
    user = UserInfoSerializer()
    class Meta:
        model = Ride
        fields = '__all__'