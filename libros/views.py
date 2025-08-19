import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Libro

def serialize_libro(libro):
    return {
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "genero": libro.genero,
        "fecha_publicacion": libro.fecha_publicacion.isoformat() if libro.fecha_publicacion else None,
    }

@csrf_exempt
def libro_list_create(request):
    if request.method == "GET":
        # Listar todos
        data = [serialize_libro(l) for l in Libro.objects.all().order_by("id")]
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        # Crear
        try:
            payload = json.loads(request.body.decode() or "{}")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("JSON inválido")

        titulo = payload.get("titulo")
        autor = payload.get("autor")
        genero = payload.get("genero", "")
        fecha_publicacion = payload.get("fecha_publicacion")  # ISO string YYYY-MM-DD o None

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

        # PATCH = parcial; PUT = completo (aquí permitimos parcial para ambos por simplicidad)
        for field in ("titulo", "autor", "genero", "fecha_publicacion"):
            if field in payload:
                setattr(libro, field, payload[field] or None)
        # Validación mínima
        if not libro.titulo or not libro.autor:
            return HttpResponseBadRequest("Campos requeridos: titulo, autor")

        libro.save()
        return JsonResponse(serialize_libro(libro), status=200)

    if request.method == "DELETE":
        libro.delete()
        return JsonResponse({"deleted": True}, status=204, safe=False)

    return HttpResponseNotAllowed(["GET", "PUT", "PATCH", "DELETE"])
