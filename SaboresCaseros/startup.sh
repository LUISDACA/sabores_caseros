#!/bin/bash
set -e

echo "📦 Aplicando migraciones..."
python manage.py migrate --noinput

echo "🗂️ Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Mostrando ubicación y paquetes instalados"
which python
python -m pip list

echo "🚀 Iniciando servidor Gunicorn..."
gunicorn SaboresCaseros.wsgi:application --bind 0.0.0.0:8000
