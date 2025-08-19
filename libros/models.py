from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
