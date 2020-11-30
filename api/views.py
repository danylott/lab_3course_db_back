from rest_framework import viewsets

from .models import Passenger, Train, Trip, Carriage, Luggage
from .serializers import PassengerSerializer, TrainSerializer, TripSerializer, CarriageSerializer, LuggageSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class CarriageViewSet(viewsets.ModelViewSet):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer


class LuggageViewSet(viewsets.ModelViewSet):
    queryset = Luggage.objects.all()
    serializer_class = LuggageSerializer
