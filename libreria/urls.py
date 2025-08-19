from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from libros.models import Libro
from libros import views as libros_views  # 👈 importa las vistas

def home(request):
    if request.user.is_authenticated:
        libros = Libro.objects.all().order_by("id")
        return render(request, "libros/index.html", {"libros": libros})
    else:
        return redirect("login")  # esta ruta la configuraremos en el siguiente paso

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("libros/", include(("libros.urls", "libros"), namespace="libros")),

    # 👇 agrega estas dos líneas:
    path("accounts/", include("django.contrib.auth.urls")),
    
    path("accounts/register/", libros_views.register, name="register"),
]

