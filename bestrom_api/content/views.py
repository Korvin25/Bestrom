from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
# Create your views here.


class GetContent (APIView):

    def get (self,request,pk,format=None):
        queryset=models.Page.objects.filter(id=pk)
        serializer=serializers.GetPageSerializer(queryset,many=True)
        return Response(serializer.data)

