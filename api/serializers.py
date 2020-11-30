from rest_framework import serializers

from .models import Passenger, Train, Trip, Carriage, Luggage


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = "__all__"


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"


class CarriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriage
        fields = "__all__"


class LuggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage
        fields = "__all__"
