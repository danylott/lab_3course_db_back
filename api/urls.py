from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from .views import PassengerViewSet, TrainViewSet, TripViewSet, CarriageViewSet, LuggageViewSet

router = DefaultRouter()

router.register('passengers', PassengerViewSet)
router.register('trains', TrainViewSet)
router.register('trips', TripViewSet)
router.register('carriages', CarriageViewSet)
router.register('luggage', LuggageViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
