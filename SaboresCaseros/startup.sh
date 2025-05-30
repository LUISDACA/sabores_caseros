#!/bin/bash
echo "✅ Aplicando migraciones..."
python manage.py migrate --noinput

echo "📦 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "🚀 Iniciando servidor Gunicorn..."
gunicorn SaboresCaseros.wsgi:application --bind 0.0.0.0:8000
