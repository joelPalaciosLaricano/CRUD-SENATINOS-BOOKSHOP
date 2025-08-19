import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView


# ---------------------------
# Funciones de utilidad
# ---------------------------
def serialize_libro(libro):
    return {
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "genero": libro.genero,
        "fecha_publicacion": libro.fecha_publicacion.isoformat() if libro.fecha_publicacion else None,
    }


# ---------------------------
# API (JSON)
# ---------------------------
@csrf_exempt
def libro_list_create(request):
    if request.method == "GET":
        data = [serialize_libro(l) for l in Libro.objects.all().order_by("id")]
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode() or "{}")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("JSON inválido")

        titulo = payload.get("titulo")
        autor = payload.get("autor")
        genero = payload.get("genero", "")
        fecha_publicacion = payload.get("fecha_publicacion")

        if not titulo or not autor:
            return HttpResponseBadRequest("Campos requeridos: titulo, autor")

        libro = Libro.objects.create(
            titulo=titulo,
            autor=autor,
            genero=genero or "",
            fecha_publicacion=fecha_publicacion or None,
        )
        return JsonResponse(serialize_libro(libro), status=201)

    return HttpResponseNotAllowed(["GET", "POST"])


def _filter_by_params(qs, params):
    titulo = params.get("titulo")
    autor = params.get("autor")
    if titulo:
        qs = qs.filter(titulo__icontains=titulo)
    if autor:
        qs = qs.filter(autor__icontains=autor)
    return qs


def libro_search(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    qs = _filter_by_params(Libro.objects.all(), request.GET)
    data = [serialize_libro(l) for l in qs.order_by("id")]
    return JsonResponse(data, safe=False)


@csrf_exempt
def libro_detail_update_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == "GET":
        return JsonResponse(serialize_libro(libro))

    if request.method in ("PUT", "PATCH"):
        try:
            payload = json.loads(request.body.decode() or "{}")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("JSON inválido")

        for field in ("titulo", "autor", "genero", "fecha_publicacion"):
            if field in payload:
                setattr(libro, field, payload[field] or None)

        if not libro.titulo or not libro.autor:
            return HttpResponseBadRequest("Campos requeridos: titulo, autor")

        libro.save()
        return JsonResponse(serialize_libro(libro), status=200)

    if request.method == "DELETE":
        libro.delete()
        return JsonResponse({"deleted": True}, status=204, safe=False)

    return HttpResponseNotAllowed(["GET", "PUT", "PATCH", "DELETE"])


# ---------------------------
# Vistas HTML (templates)
# ---------------------------
def libro_list_view(request):
    q = request.GET.get("q", "")
    orden = request.GET.get("orden", "titulo")  # valor por defecto: título
    direccion = request.GET.get("dir", "asc")

    # aplicamos filtros
    libros = Libro.objects.all()
    if q:
        libros = libros.filter(titulo__icontains=q) | libros.filter(autor__icontains=q)

    # aplicamos ordenamiento
    if direccion == "desc":
        orden = f"-{orden}"
    libros = libros.order_by(orden)

    return render(
        request,
        "libros/libro_list.html",
        {"libros": libros, "q": q, "direccion": direccion}
    )


def libro_create_view(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libros:libro-list")
    else:
        form = LibroForm()
    return render(request, "libros/libro_form.html", {"form": form})


def libro_update_view(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect("libros:libro-list")
    else:
        form = LibroForm(instance=libro)
    return render(request, "libros/libro_form.html", {"form": form})


def libro_delete_view(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        libro.delete()
        return redirect("libros:libro-list")
    return render(request, "libros/libro_confirm_delete.html", {"libro": libro})


# ---------------------------
# Registro de usuarios
# ---------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente
            messages.success(
                request,
                f"✅ BIENVENIDO AL SISTEMA DE GESTIÓN DE LIBROS, {user.username.upper()} 🎉"
            )
            return redirect("libros:libro-list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


# ---------------------------
# Login personalizado con mensaje
# ---------------------------
class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        messages.success(
            self.request,
            f"✅ BIENVENIDO AL SISTEMA DE GESTIÓN DE LIBROS, {user.username.upper()} 🎉"
        )
        return super().form_valid(form)
