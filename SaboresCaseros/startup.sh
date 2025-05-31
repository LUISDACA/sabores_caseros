#!/bin/bash

echo "🔁 Instalando dependencias..."
pip install -r requirements.txt

echo "🚀 Migrando base de datos..."
python manage.py migrate --noinput

echo "📦 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "🔥 Ejecutando Gunicorn en puerto 8000..."
exec gunicorn SaboresCaseros.wsgi:application --bind=0.0.0.0:8000
