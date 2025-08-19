from django.urls import path
from . import views

app_name = "libros"

urlpatterns = [
    path("", views.LibroListView.as_view(), name="libro_list"),
]
