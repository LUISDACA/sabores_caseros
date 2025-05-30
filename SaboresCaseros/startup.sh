#!/bin/bash

echo "✅ Activando entorno virtual (si aplica)"
if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "📦 Aplicando migraciones..."
python manage.py migrate --noinput

echo "🗂️ Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "🚀 Iniciando servidor Gunicorn..."
exec gunicorn SaboresCaseros.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 600 \
    --log-level info
