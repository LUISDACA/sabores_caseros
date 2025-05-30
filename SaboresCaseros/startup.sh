#!/bin/bash
set -e

echo "📦 Aplicando migraciones..."
python manage.py migrate --noinput

echo "🗂️ Recolectando archivos estáticos..."
python manage.py collectstatic --noinput
