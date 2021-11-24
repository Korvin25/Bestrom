from rest_framework import serializers
from . import models

class CrmFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Crm_forms
        fields='__all__'