from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Bestrom API",
      default_version='v1',
      description="Description for development",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bexram33@mail.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
   path('ckeditor/', include('ckeditor_uploader.urls')),
   path('api/', include('content.urls')),
   path('api/', include('product.urls')),
   path('api/', include('crm.urls')),
]
