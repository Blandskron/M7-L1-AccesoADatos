# Proyecto Django Educativo

Este proyecto tiene como objetivo enseñar a configurar y utilizar Django para trabajar con bases de datos, realizar consultas SQL y aprovechar el potencial del ORM (Object Relational Mapper) de Django. También incluye una introducción al soporte para bases NoSQL como MongoDB.

## Tecnologías utilizadas

- **Django**: Framework web en Python.
- **SQLite**: Base de datos por defecto.
- **PostgreSQL**: Base de datos relacional avanzada (opcional).
- **MongoDB**: Base de datos NoSQL (opcional).

## Configuración inicial

1. **Crear el proyecto Django**

   Ejecuta los siguientes comandos en tu terminal para iniciar un proyecto Django:
   ```bash
   django-admin startproject educational_project
   cd educational_project
   python manage.py startapp school
   ```

2. **Configurar la base de datos**

   En el archivo `educational_project/settings.py`, agrega la configuración de la base de datos. Por defecto, se utiliza SQLite:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': 'cu07',
           'USER': 'user07',
           'PASSWORD': 'user07_password',
           'HOST': '',
           'PORT': '',
       }
   }
   ```

   Si prefieres PostgreSQL, usa esta configuración:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'educational_db',
           'USER': 'postgres',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Soporte para MongoDB (Opcional)**

   Para trabajar con MongoDB, instala el paquete `djongo`:
   ```bash
   pip install djongo
   ```

   Configura `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'educational_db',
       }
   }
   ```

## Crear el modelo educativo

Define los modelos en el archivo `school/models.py`:
```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    enrollment_date = models.DateField(auto_now_add=True)

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name
```

Ejecuta las migraciones para aplicar estos cambios a la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Crear vistas para consultas SQL

En el archivo `school/views.py`, crea vistas para ejecutar consultas SQL personalizadas:
```python
from django.shortcuts import render
from django.db import connection
from .models import Student

def custom_sql_query(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM school_student WHERE age > %s", [18])
        rows = cursor.fetchall()

    return render(request, 'students.html', {'students': rows})

def raw_query_example(request):
    students = Student.objects.raw('SELECT * FROM school_student WHERE age < %s', [18])
    return render(request, 'students.html', {'students': students})
```

## Configurar URLs

En el archivo `educational_project/urls.py`, registra las rutas para las vistas:
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-query/', views.custom_sql_query, name='custom_query'),
    path('raw-query/', views.raw_query_example, name='raw_query'),
]
```

## Crear plantillas HTML

En la carpeta `school/templates/`, crea un archivo `students.html` para mostrar los resultados:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Students</title>
</head>
<body>
    <h1>Student List</h1>
    <ul>
        {% for student in students %}
            <li>{{ student }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Ejecutar el servidor

Para iniciar el servidor y probar las rutas configuradas:
```bash
python manage.py runserver
```

Accede a las rutas configuradas en tu navegador:
- [http://localhost:8000/custom-query/](http://localhost:8000/custom-query/): Para consultas SQL personalizadas con `connection.cursor()`.
- [http://localhost:8000/raw-query/](http://localhost:8000/raw-query/): Para consultas SQL usando `Manager.raw()`.

## Conclusión

Este proyecto demuestra cómo:
1. Configurar bases de datos en Django (SQLite, PostgreSQL y MongoDB).
2. Crear modelos para manejar datos educativos.
3. Ejecutar consultas SQL personalizadas utilizando las herramientas que ofrece Django.

Es ideal para propósitos educativos y como base para proyectos más avanzados.

