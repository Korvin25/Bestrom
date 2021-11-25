from django.urls import path
from . import views

urlpatterns = [
    path('filters/', views.GetFilters.as_view()),
    path('product/', views.GetListProduct.as_view()),
    # path('product/<int:pk>/', views.GetDetailProduct.as_view()),
    path('packets/', views.GetPacket.as_view()),
    path('packetoptions/', views.GetPacketOptions.as_view()),
    path('packetseams/', views.GetPacketOptions.as_view()),
]
