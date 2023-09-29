from .base import *
import os
from dotenv import load_dotenv
load_dotenv()

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),         # Reemplaza con el nombre de tu base de datos
        'USER': os.getenv("DB_USER"),         # Reemplaza con tu nombre de usuario de PostgreSQL
        'PASSWORD': os.getenv("DB_PASSWD"),   # Reemplaza con tu contraseña de PostgreSQL
        'HOST': os.getenv("DB_HOST"),         # Reemplaza con la dirección de tu servidor PostgreSQL
        'PORT':  os.getenv("DB_PORT")         # Reemplaza con el puerto de PostgreSQL (generalmente 5432)
    }
}

TIME_ZONE = 'America/Bogota'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }