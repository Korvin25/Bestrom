from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Crm_forms
from .serializers import CrmFormsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class FormsList(generics.ListCreateAPIView):
    queryset = Crm_forms.objects.all()
    serializer_class = CrmFormsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class FormsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crm_forms.objects.all()
    serializer_class = CrmFormsSerializer