from django.urls import path
from django.urls import re_path
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Event management",
      default_version='v0.1',
      description="Test backend by isa",
      contact=openapi.Contact(email="5carlosmoreno2021@gmail.com"),
      license=openapi.License(name="OPEN SOURCE ALLOW"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatternsSwagger = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path("", lambda request: redirect("swagger/", permanent=False)),
]