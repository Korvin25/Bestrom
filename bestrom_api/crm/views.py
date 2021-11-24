from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Crm_forms
from .serializers import CrmFormsSerializer


class FormsList(generics.ListCreateAPIView):
    queryset = Crm_forms.objects.all()
    serializer_class = CrmFormsSerializer


class FormsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crm_forms.objects.all()
    serializer_class = CrmFormsSerializer