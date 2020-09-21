from rest_framework import serializers


class RatSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=32)
    variety = serializers.CharField(max_length=128)
    gender = serializers.CharField(max_length=8)
    title = serializers.CharField(max_length=16)
    date_of_birth = serializers.DateField()
    date_of_death = serializers.DateField()
    in_rattery = serializers.BooleanField()
    castrate = serializers.BooleanField()
    information = serializers.CharField(max_length=2048)


class LitterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=8)
    number = serializers.CharField(max_length=16)
    date_of_birth = serializers.DateField()