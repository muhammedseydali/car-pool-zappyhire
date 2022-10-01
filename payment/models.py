from django.db import models
from accounts.models import Account
# Create your models here.

class Payments(models.Model):
    user = models.ForeignKey(Account, related_name='Payments')
    payer = models.CharField(max_length=255, blank=True)
    paymet_id = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
