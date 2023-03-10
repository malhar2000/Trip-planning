from django.db import models
from uuid import uuid4

# Create your models here.
class Trip(models.Model):
    trip_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    trip_start_time = models.DateTimeField(auto_now=True, blank=True)
    trip_end_time = models.DateTimeField(auto_now=True, blank=True)
    trip_start_station_name = models.CharField(max_length=100)
    trip_end_station_name = models.CharField(max_length=100)
    trip_title = models.CharField(max_length=100)

    def __str__(self):
        return self.trip_title

class TripDetails(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    trip_details_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    trip_details_time = models.DateTimeField(auto_now=True, blank=True)
    trip_details_location_to_visit = models.CharField(max_length=100)
    trip_location_budget = models.IntegerField()
    trip_members = models.IntegerField()
   
    
     