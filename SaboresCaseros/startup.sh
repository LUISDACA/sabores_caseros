#!/bin/bash
echo "✅ Activando entorno virtual (si aplica)"
echo "📦 Aplicando migraciones..."
python manage.py migrate --noinput

echo "🗂️ Recolectando archivos estáticos..."
python manage.py collectstatic --noinput
