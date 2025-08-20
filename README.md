# CRUD-SENATINOS-BOOKSHOP

Este proyecto es una aplicación web desarrollada con Django para la gestión de libros en una librería. A continuación se describe la estructura de carpetas y archivos, junto con su función principal.

## Estructura del Proyecto

```
CRUD-SENATINOS-BOOKSHOP/
│
├── env/                  # Entorno virtual de Python con dependencias instaladas
│   ├── Scripts/          # Ejecutables y scripts de activación/desactivación
│   ├── Lib/              # Paquetes y librerías instaladas
│   └── ...               # Archivos de configuración del entorno
│
├── libreria/             # Configuración principal del proyecto Django
│   ├── asgi.py           # Configuración para ASGI (servidores asíncronos)
│   ├── init.py           # Inicialización del paquete
│   ├── settings.py       # Configuración general del proyecto (BD, apps, rutas, etc.)
│   ├── urls.py           # Rutas principales del proyecto
│   ├── wsgi.py           # Configuración para WSGI (servidores síncronos)
│   └── __pycache__/      # Archivos compilados por Python
│
├── libros/               # Aplicación principal para la gestión de libros
│   ├── admin.py          # Configuración del panel de administración de Django
│   ├── forms.py          # Formularios personalizados para la app
│   ├── init.py           # Inicialización del paquete
│   ├── models.py         # Definición de modelos (tablas de la BD)
│   ├── tests.py          # Pruebas unitarias de la app
│   ├── urls.py           # Rutas específicas de la app libros
│   ├── views.py          # Lógica de las vistas (CRUD de libros)
│   ├── migrations/       # Migraciones de la base de datos
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_libro_editorial_libro_isbn.py
│   │   └── __pycache__/
│   └── __pycache__/      # Archivos compilados por Python
│
├── static/               # Archivos estáticos (CSS, imágenes, JS)
│   ├── css/
│   │   └── estilos.css   # Estilos personalizados para la web
│   └── img/
│       └── libros.jpg    # Imagen utilizada en la web
│
├── templates/            # Plantillas HTML para renderizar las vistas
│   ├── base.html         # Plantilla base para herencia
│   ├── libros/           # Plantillas específicas de la app libros
│   │   ├── index.html
│   │   ├── libro_confirm_delete.html
│   │   ├── libro_form.html
│   │   └── libro_list.html
│   └── registration/     # Plantillas para autenticación de usuarios
│       ├── logged_out.html
│       ├── login.html
│       ├── register.html
│       └── styles.css    # Estilos para formularios de registro/login
│
└── README.md             # Documentación del proyecto
```

## Descripción de Carpetas y Archivos

- **env/**: Entorno virtual con todas las dependencias necesarias para ejecutar el proyecto.
- **libreria/**: Configuración principal del proyecto Django.
- **libros/**: Aplicación Django para gestionar libros (CRUD, modelos, formularios, vistas, rutas).
- **static/**: Archivos estáticos como hojas de estilo CSS e imágenes.
- **templates/**: Plantillas HTML para las vistas y formularios del proyecto.
- **README.md**: Este archivo de documentación.

## Cómo ejecutar el proyecto

1. Activa el entorno virtual:
   - Windows:  
     ```
     .\env\Scripts\activate
     ```
2. Instala las dependencias (si es necesario):
   ```
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```
   python manage.py migrate
   ```
4. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

---

**Autor: Yo y El**
