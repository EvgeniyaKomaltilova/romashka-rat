from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import RatSerializer, LitterSerializer
from rattery.models.Litter import Litter
from rattery.models.Rat import Rat


class RatView(APIView):

    def get(self, request):
        rats = Rat.objects.filter(public=True)
        serializer = RatSerializer(rats, many=True)
        return Response({"rats": serializer.data})


class LitterView(APIView):

    def get(self, request):
        litters = Litter.objects.filter(public=True)
        serializer = LitterSerializer(litters, many=True)
        return Response({"litters": serializer.data})
