from django.conf.urls import include
from django.urls import path
from .import views


urlpatterns = [
   path('create_ride/', views.Ride_Create.as_view(), name='ride'),
   path('get_rides/', views.get_rides, name='get_rides'),
   

]