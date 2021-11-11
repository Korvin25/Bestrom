from django.urls import path
from . import views

urlpatterns = [
    path('filters/', views.GetFilters.as_view()),
    path('product/', views.GetListProduct.as_view()),
    path('product/<int:pk>/', views.GetDetailProduct.as_view()),
]
