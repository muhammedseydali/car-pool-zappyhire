from django.conf.urls import include
from django.urls import path
from .import views


urlpatterns = [
   path('create_ride/', views.Ride_Create.as_view(), name='ride'),

   path('get_rides/', views.get_rides, name='get_rides'),

   path('get_rides_object/<int:id>', views.get_rides_object, name='get_rides_object'),

   path('send_ride_request/<int:user_id>', views.send_ride_request, name='send_ride_request'), 
 
   path('accept_ride_request/<int:id>', views.accept_ride_request, name='accept_ride_request'  ),

   path('list_all_rides', views.list_all_rides, name='list_all_rides'), 


]