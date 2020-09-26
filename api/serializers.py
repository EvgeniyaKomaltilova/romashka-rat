from rest_framework import serializers
from rattery.models.Litter import Litter
from rattery.models.Location import Location
from rattery.models.Person import Person
from rattery.models.Prefix import Prefix
from rattery.models.Rat import Rat


class RatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rat
        fields = (
            'id',
            'in_rattery',
            'litter',
            'name',
            'prefix',
            'variety',
            'gender',
            'title',
            'date_of_birth',
            'date_of_death',
            'breeder',
            'owner',
            'father',
            'mother',
            'information')


class LitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Litter
        fields = (
            'id',
            'name',
            'prefix',
            'number',
            'date_of_birth',
            'year',
            'father',
            'mother',
            'breeder')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'last_name',
            'first_name',
            'second_name',
            'location')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'country',
            'region',
            'city')


class PrefixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefix
        fields = (
            'female_name',
            'male_name',
            )
