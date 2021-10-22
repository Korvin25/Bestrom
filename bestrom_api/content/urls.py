from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:pk>/', views.GetContent.as_view()),
    path('news/', views.GetNews.as_view()),
    path('client/', views.GetClient.as_view()),
    path('partner/', views.GetPartner.as_view()),
    path('vacancy/', views.GetNews.as_view()),
]
