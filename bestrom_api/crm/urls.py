from django.urls import path
from . import views

urlpatterns = [
    # path('forms/', views.FormsList.as_view()),
    # path('forms/<int:pk>/', views.FormsDetail.as_view()),
    path('forms/', views.forms_list),  # Для GET и POST запросов
    path('forms/<int:pk>/', views.forms_detail),  # Для GET, PUT и DELETE запросов
]
