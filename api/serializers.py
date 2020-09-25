from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from rattery.models.Rat import Rat


class RatSerializer(serializers.Serializer):

    old_id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)
    prefix_id = serializers.IntegerField()
    variety = serializers.CharField(max_length=128)
    gender = serializers.CharField(max_length=8)
    title = serializers.CharField(max_length=16)
    date_of_birth = serializers.DateField()
    date_of_death = serializers.DateField()
    breeder = serializers.IntegerField()
    owner = serializers.IntegerField()
    father = serializers.IntegerField()
    mother = serializers.IntegerField()
    in_rattery = serializers.BooleanField()
    castrate = serializers.BooleanField()
    information = serializers.CharField(max_length=2048)

    def create(self, validated_data):
        return Rat.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.prefix_id = validated_data.get('prefix_id', instance.prefix_id)
        instance.variety = validated_data.get('variety', instance.variety)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.title = validated_data.get('title', instance.title)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.date_of_death = validated_data.get('date_of_death', instance.date_of_death)
        instance.breeder = validated_data.get('breeder', instance.breeder)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.father = validated_data.get('father', instance.father)
        instance.mother = validated_data.get('mother', instance.mother)
        instance.in_rattery = validated_data.get('in_rattery', instance.in_rattery)
        instance.castrate = validated_data.get('castrate', instance.castrate)
        instance.information = validated_data.get('information', instance.information)
        instance.save()
        return instance

    def put(self, request, pk):
        saved_rat = get_object_or_404(Rat.objects.all(), pk=pk)
        data = request.data.get('rat')
        serializer = RatSerializer(instance=saved_rat, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            rat_saved = serializer.save()
        return Response({"success": "Rat '{}' updated successfully".format(rat_saved.title)})

    def delete(self, request, pk):
        rat = get_object_or_404(Rat.objects.all(), pk=pk)
        rat.delete()
        return Response(
            {"message": "Rat with id `{}` has been deleted.".format(pk)},
            status=204)


class LitterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=8)
    number = serializers.CharField(max_length=16)
    date_of_birth = serializers.DateField()