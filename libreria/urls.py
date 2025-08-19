from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(_):
    return JsonResponse({"ok": True, "service": "Libreria API"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("libros/", include(("libros.urls", "libros"), namespace="libros")),
]

