from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from .models import Crm_forms
from .serializers import CrmFormsSerializer
from django.http import JsonResponse, HttpResponse
from .models import Crm_forms
import json


@csrf_exempt
def forms_list(request):
    """
    Обрабатывает GET и POST запросы для списка заявок.
    """
    if request.method == 'GET':
        forms = Crm_forms.objects.all()
        data = [{
            'id': form.id,
            'dateapp': form.dateapp,
            'type': form.type,
            'telephone': form.telephone,
            'email': form.email,
            'name': form.name,
            'other': form.other,
            'file': form.file.url if form.file else None,
        } for form in forms]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = Crm_forms.objects.create(
                type=data.get('type'),
                telephone=data.get('telephone'),
                email=data.get('email'),
                name=data.get('name'),
                other=data.get('other'),
                file=data.get('file'),
            )
            return JsonResponse({
                'id': form.id,
                'dateapp': form.dateapp,
                'type': form.type,
                'telephone': form.telephone,
                'email': form.email,
                'name': form.name,
                'other': form.other,
                'file': form.file.url if form.file else None,
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def forms_detail(request, pk):
    """
    Обрабатывает GET, PUT и DELETE запросы для конкретной заявки.
    """
    try:
        form = Crm_forms.objects.get(pk=pk)
    except Crm_forms.DoesNotExist:
        return JsonResponse({'error': 'Заявка не найдена'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': form.id,
            'dateapp': form.dateapp,
            'type': form.type,
            'telephone': form.telephone,
            'email': form.email,
            'name': form.name,
            'other': form.other,
            'file': form.file.url if form.file else None,
        })

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            form.type = data.get('type', form.type)
            form.telephone = data.get('telephone', form.telephone)
            form.email = data.get('email', form.email)
            form.name = data.get('name', form.name)
            form.other = data.get('other', form.other)
            form.file = data.get('file', form.file)
            form.save()
            return JsonResponse({
                'id': form.id,
                'dateapp': form.dateapp,
                'type': form.type,
                'telephone': form.telephone,
                'email': form.email,
                'name': form.name,
                'other': form.other,
                'file': form.file.url if form.file else None,
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'DELETE':
        form.delete()
        return HttpResponse(status=204)

# class FormsList(generics.ListCreateAPIView):
#     queryset = Crm_forms.objects.all()
#     serializer_class = CrmFormsSerializer


# class FormsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Crm_forms.objects.all()
#     serializer_class = CrmFormsSerializer