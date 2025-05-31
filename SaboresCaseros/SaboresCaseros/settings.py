import os
from pathlib import Path
from datetime import timedelta
from decouple import config
import dj_database_url
from ast import literal_eval

BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad y entorno
SECRET_KEY = config('SECRET_KEY', default='clave-insegura')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'storages',  # 👈 necesario para Azure Blob Storage
    'sabores',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SaboresCaseros.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SaboresCaseros.wsgi.application'

# Base de datos (puedes adaptar para PostgreSQL en Azure, Railway, etc.)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbsabores',
        'USER': 'dbsabores_user',
        'PASSWORD': 'amkgY2lOGpCmFRxQ4DykIBmc7iAG0anF',
        'HOST': 'dpg-d0t8njadbo4c739dsfug-a.virginia-postgres.render.com',
        'PORT': '5432',
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Archivos media (modo desarrollo)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Media en modo producción con Azure Blob Storage
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'sabores.storage.AzureMediaStorage'
    AZURE_ACCOUNT_NAME = config('AZURE_ACCOUNT_NAME')
    AZURE_ACCOUNT_KEY = config('AZURE_ACCOUNT_KEY')
    AZURE_CONTAINER = config('AZURE_CONTAINER')
    AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"
    MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_CONTAINER}/"

# Modelo personalizado
AUTH_USER_MODEL = 'sabores.Usuario'

# DRF + JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# CORS frontend en Azure Static Web Apps
CORS_ALLOWED_ORIGINS = [
    "https://icy-field-005c64a1e.6.azurestaticapps.net",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
