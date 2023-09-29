from django.contrib import admin
from .config_swagger import urlpatternsSwagger
from django.urls import path, include


urlpatterns = urlpatternsSwagger + [
    path("admin/", admin.site.urls),
    path("api/", include("apps.events.routers")),
]
