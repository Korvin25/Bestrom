from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.GetListProduct.as_view()),
    path('product/<int:pk>/', views.GetDetailProduct.as_view()),
]
