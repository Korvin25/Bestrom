from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class GetListProduct(APIView):
    def get(self, request, format=None):
        queryset = models.Product.objects.all()
        serializer = serializers.ListProductSerializer(queryset, many=True)
        return Response(serializer.data)


class GetDetailProduct(APIView):
    def get(self, request, pk, format=None):
        queryset = models.Product.objects.get(id=pk)
        serializer = serializers.DetailProductSerializer(queryset, many=False)
        return Response(serializer.data)


class GetFilters(generics.ListAPIView):
    queryset = models.CategoryFilter.objects.all()
    serializer_class = serializers.CategoryFilterSerializer
