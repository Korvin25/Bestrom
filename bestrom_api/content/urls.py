from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:pk>/', views.GetContent.as_view()),
]
