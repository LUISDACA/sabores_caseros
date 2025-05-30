#!/bin/bash

echo "🚀 Iniciando servidor Gunicorn..."

# Exportar variables necesarias si no están ya en el entorno
export DJANGO_SETTINGS_MODULE=SaboresCaseros.settings
export PYTHONUNBUFFERED=1

# Ejecutar migraciones y recopilar archivos estáticos
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Iniciar Gunicorn en el puerto 8000
exec gunicorn SaboresCaseros.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120
