from django.db import models
from accounts.models import Account
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Ride(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    source_city = models.CharField(max_length=255, blank=True)
    destination_city = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    time = models.TimeField(unique=True)
    seat = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.source_city)


class RideRequest(models.Model):
    from_user = models.ForeignKey(Account, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Account, related_name='to_user', on_delete=models.CASCADE)
    ride_id = models.ForeignKey(Ride, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.from_user)
        

class Copassenger(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE) 
    passenger_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.passenger_name)       
    
