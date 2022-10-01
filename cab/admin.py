from turtle import right
from .models import Ride, RideRequest, Copassenger
from django.contrib import admin
# Register your models here.


class RideAdmin(admin.ModelAdmin):
    model = Ride
    list_display = ('user', 'source_city', 'destination_city', 'date', 'time', 'seat', 'amount') 

    filter_horizontal =()
    list_filter = ()
    fieldsets =()

admin.site.register(Ride, RideAdmin)    


class RideRequestAdmin(admin.ModelAdmin):
    model = RideRequest
    list_display = ('from_user', 'to_user', 'ride_id') 

    filter_horizontal =()
    list_filter = ()
    fieldsets =()

admin.site.register(RideRequest, RideRequestAdmin)  


class CopassengerAdmin(admin.ModelAdmin):
    model = Copassenger
    list_display = ('ride', 'passenger_name') 

    filter_horizontal =()
    list_filter = ()
    fieldsets =()

admin.site.register(Copassenger, CopassengerAdmin) 

  
    
