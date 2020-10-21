--- DJANGO CURSO PLATZI ---
Framework = nace de la poca escalabilidad de los lenguajes como php (se repetia mucho codigo)
Resuelven tareas en eld esarrollo web: peticion http, creacion de respuesta, consulta a base de datos,
interaccion con html, djang agrega sistemas de usuarios

- Mantener sitios grandes (facil)
- Urls bien diseñadas
- http request - http Response
- muchos sitios en poco tiempo
- ORM, permite conectarte a la base de datos

Para instalarlo instalamos python 3.7
pip3 - para validar que existen (la version de pip debe coincidir con la de python)
Genero mi entorno virtual

python3 -m venv .env (me genera una carpeta oculta, entro)

MacBook-Air-de-Ignacio-2:.env ignaciobellucci$ ls -l
total 16
drwxr-xr-x  15 ignaciobellucci  staff  510 Aug 20 21:21 bin
drwxr-xr-x   2 ignaciobellucci  staff   68 Aug 20 21:18 include
drwxr-xr-x   3 ignaciobellucci  staff  102 Aug 20 21:18 lib
-rw-r--r--   1 ignaciobellucci  staff   59 Aug 20 21:21 pip-selfcheck.json
-rw-r--r--   1 ignaciobellucci  staff  114 Aug 20 21:18 pyvenv.cfg
MacBook-Air-de-Ignacio-2:.env ignaciobellucci$ pwd
/Users/ignaciobellucci/Desktop/.env

MacBook-Air-de-Ignacio-2:bin ignaciobellucci$ source activate
(.env) MacBook-Air-de-Ignacio-2:bin ignaciobellucci$ pwd
/Users/ignaciobellucci/Desktop/.env/bin

deactive para desactivar

instalamos DJANGO
pip install django -U (-u para que sea la ultima version)

Revisamos que librerias tengo en mi entorno virtual:
(.env) MacBook-Air-de-Ignacio-2:bin ignaciobellucci$ pip3 freeze
Django==2.1
pytz==2018.5

el comando central de django es: django-admin: nos da todas las opciones

Lanzamos nuestro proyecto nuevo: django-admin startproyect platzigram
Esto nos crea dos archivos que son, platzigram y manage.py
dentro de platzigram tenemos:

__init__.py que esta vacio y solamente existe para tratarlo como un modulo de python

settings.py define configuraciones de django
BASE_DIR = Corre el proyecto
SECRET_KEY = hash de las contraseñas y sesiones de base de datos
DEBUG = True # nos agrega mas info Poner en false cuando esta en PROD
ALLOWED_HOST: host permitidos
INSTALLED_APPS = app instaladas o ligadas a nuestro proyecto de DJANGO
ROOT_URLCONF = definimos modulo de entrada
TEMPLATES= config de tempaltes
WSGI_APP = nuestro archivo de entrada de deploy
DATABASES = poner la base que necesitamos y poner credenciales de acceso
AUTH_PASSWORD = validares de contraseña (es para validar que contraseña se pone requisitos y demas)

LANGUAGE = que idioma corre nuestra aplicacion
TOME_ZONE
USE_L1ON para traduccion
STATIC_URL = '/static' busca el archivo static

urls.py nuestro archivo principal de entrada para todas las peticiones que ingresen a nuestro proyecto

wsgi.py el archivo de django para los deploy

manage.py NUNCA SE TOCA pero interactuamos es una interfaz

python3 manage.py nos tira los comandos de las aplicaciones o herramientas ue nos sirve

python3 manage.py runserver
http://localhost:8000/

UNA VISTA EN DJANGO es una funcion

trabajamos con urls.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!!")

urlpatterns = [

    path('hello-world',hello_world)

]

http://127.0.0.1:8000/hello-world
