from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class GetListProduct(APIView):
    def get(self, request, format=None):
        queryset = models.Product.objects.filter(active=True)
        serializer = serializers.DetailProductSerializer(queryset, many=True)
        return Response(serializer.data)


class GetDetailProduct(APIView):
    def get(self, request, pk, format=None):
        queryset = models.Product.objects.get(id=pk)
        serializer = serializers.DetailProductSerializer(queryset, many=False)
        return Response(serializer.data)


class GetFilters(generics.ListAPIView):
    queryset = models.CategoryFilters.objects.all()
    serializer_class = serializers.CategoryFilterSerializer


class GetPacket(generics.ListAPIView):
    queryset = models.Packet.objects.all()
    serializer_class = serializers.PacketSerializer


class GetPacketOptions(generics.ListAPIView):
    queryset = models.PacketOptions.objects.all()
    serializer_class = serializers.PacketOptionsSerializer


class GetPacketSeam(generics.ListAPIView):
    queryset = models.PacketSeam.objects.all()
    serializer_class = serializers.PacketSeamSerializer
