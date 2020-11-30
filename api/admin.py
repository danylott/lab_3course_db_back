from django.contrib import admin

from .models import Passenger, Train, Trip, Carriage, Luggage


admin.site.register(Passenger)
admin.site.register(Train)
admin.site.register(Trip)
admin.site.register(Carriage)
admin.site.register(Luggage)
