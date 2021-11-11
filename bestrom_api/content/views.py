from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


# Create your views here.


class GetContent(APIView):

    def get(self, request, pk, format=None):
        queryset = models.Page.objects.filter(id=pk)
        serializer = serializers.GetPageSerializer(queryset, many=True)
        return Response(serializer.data)


class GetNews(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.GetNewsSerializer


class GetVacancy(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.GetVacancySerializer


class GetClient(generics.ListAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.GetClientSerializer


class GetPartner(generics.ListAPIView):
    queryset = models.Partner.objects.all()
    serializer_class = serializers.GetPartnerSerializer


class GetHistory(generics.ListAPIView):
    queryset = models.History.objects.all()
    serializer_class = serializers.GetHistorySerializer


