from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Libro

# --- Formulario para libros ---
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "genero", "fecha_publicacion"]
        widgets = {
            "fecha_publicacion": forms.DateInput(attrs={"type": "date"}),
        }

# --- Formulario para usuarios ---
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingrese un correo válido.")

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
