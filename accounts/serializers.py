from operator import attrgetter
from .models import Account
from django.db import transaction
from rest_framework import fields, serializers
    
class UserRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    profile_picture = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Account
        fields = ['id','username','phone_number','email','dob','profile_picture','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    
    def save(self):
        with transaction.atomic():
            reg = Account(
                email=self.validated_data['email'],
                phone_number=self.validated_data['phone_number'],
                dob=self.validated_data['dob'],
                username=self.validated_data['username'],
                profile_picture=self.validated_data['profile_picture'],
            )
            if Account.objects.filter(phone_number=self.validated_data['phone_number']).exists():
                raise serializers.ValidationError({'error':'phone number already registered!!'})
            password=self.validated_data['password']
            password2=self.validated_data['password2']
            
            if password != password2:
                raise serializers.ValidationError({'error':'password does not match!!'})
            reg.set_password(password)
            reg.save()
        return reg
 
 
    
class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Account
        fields=['id','username','phone_number','email','dob','profile_picture']