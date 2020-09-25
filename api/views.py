from rest_framework import viewsets
from api.serializers import RatSerializer, LitterSerializer, LocationSerializer, PersonSerializer, PrefixSerializer
from rattery.models.Litter import Litter
from rattery.models.Location import Location
from rattery.models.Person import Person
from rattery.models.Prefix import Prefix
from rattery.models.Rat import Rat


class RatViewSet(viewsets.ModelViewSet):
    queryset = Rat.objects.filter(public=True)
    serializer_class = RatSerializer


class LitterViewSet(viewsets.ModelViewSet):
    queryset = Litter.objects.filter(public=True)
    serializer_class = LitterSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PrefixViewSet(viewsets.ModelViewSet):
    queryset = Prefix.objects.all()
    serializer_class = PrefixSerializer
