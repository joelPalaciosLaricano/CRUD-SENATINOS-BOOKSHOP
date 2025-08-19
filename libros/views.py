from django.http import JsonResponse
from django.views import View
from .models import Libro

class LibroListView(View):
    def get(self, request):
        data = list(Libro.objects.values("id", "titulo", "autor"))
        return JsonResponse(data, safe=False)
