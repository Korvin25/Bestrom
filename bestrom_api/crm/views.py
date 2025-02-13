from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from .models import Crm_forms
from .serializers import CrmFormsSerializer

@csrf_exempt
class FormsList(generics.ListCreateAPIView):
    queryset = Crm_forms.objects.all()
    serializer_class = CrmFormsSerializer

@csrf_exempt
class FormsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crm_forms.objects.all()
    serializer_class = CrmFormsSerializer