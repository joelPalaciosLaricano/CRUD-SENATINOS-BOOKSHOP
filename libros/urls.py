from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import CustomLoginView

app_name = "libros"

urlpatterns = [
    # ---------------------------
    # API (JSON)
    # ---------------------------
    path("api/", views.libro_list_create, name="api-libro-list-create"),   # GET list / POST create
    path("api/buscar/", views.libro_search, name="api-libro-search"),
    path("api/<int:pk>/", views.libro_detail_update_delete, name="api-libro-detail"),

    # ---------------------------
    # HTML (templates)
    # ---------------------------
    path("", views.libro_list_view, name="libro-list"),                     # Lista HTML
    path("crear/", views.libro_create_view, name="libro-create"),           # Crear HTML
    path("<int:pk>/editar/", views.libro_update_view, name="libro-update"), # Editar HTML
    path("<int:pk>/eliminar/", views.libro_delete_view, name="libro-delete"), # Eliminar HTML

    # ---------------------------
    # Autenticación
    # ---------------------------
    path("login/", CustomLoginView.as_view(), name="login"),   # Login con mensaje personalizado
    path("logout/", LogoutView.as_view(next_page="libros:login"), name="logout"),  # Logout
    path("register/", views.register, name="register"),  # Registro de usuario
]
