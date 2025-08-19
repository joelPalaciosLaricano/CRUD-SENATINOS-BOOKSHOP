import datetime
import pytest
from libros.models import Libro

@pytest.mark.django_db
def test_crear_libro():
    libro = Libro.objects.create(
        titulo="El Quijote",
        autor="Cervantes",
        fecha_publicacion=datetime.date(1605, 1, 16)  # 👈 aquí
    )
    assert libro.titulo == "El Quijote"


@pytest.mark.django_db
def test_vista_lista_libros(client):
    Libro.objects.create(
        titulo="1984",
        autor="Orwell",
        fecha_publicacion=datetime.date(1949, 6, 8)  # 👈 aquí
    )
    response = client.get("/libros/")
    assert response.status_code == 200
    assert "1984" in response.content.decode()
