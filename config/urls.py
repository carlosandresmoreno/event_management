from django.contrib import admin
from django.urls import path
from .config_swagger import urlpatternsSwagger

urlpatterns = urlpatternsSwagger + [
    path("admin/", admin.site.urls),
    # path("api-sigi/", include("apps.plan.routers")),
    # path("api-sigi/", include("apps.orders.routers")),
]
