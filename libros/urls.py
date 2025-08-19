from django.urls import path
from . import views

app_name = "libros"

urlpatterns = [
    path("", views.libro_list_create, name="libro_list"),                 # GET list / POST create
    path("buscar/", views.libro_search, name="libro_search"),             # GET search
    path("<int:pk>/", views.libro_detail_update_delete, name="libro_detail"),  # GET / PUT / PATCH / DELETE
]
