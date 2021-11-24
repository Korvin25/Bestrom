from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.FormsList.as_view()),
    path('forms/<int:pk>/', views.FormsDetail.as_view()),
]
