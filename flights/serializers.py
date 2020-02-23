from .models import Flight, Booking
from rest_framework import serializers


class FlightSerializers (serializers.ModelSerializer) :
    class Meta :
        model = Flight
        fields = ['id', 'destination', 'time', 'price']

class BookingSerializers (serializers.ModelSerializer) :
    class Meta :
        model = Booking
        fields = ['id','flight','date']
