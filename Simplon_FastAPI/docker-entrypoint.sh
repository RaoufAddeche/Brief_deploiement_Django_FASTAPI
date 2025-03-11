#!/bin/bash
set -e

# Attendre que la base de données soit prête (si nécessaire)
echo "Waiting for database..."
sleep 5

# Appliquer les migrations Alembic
echo "Applying database migrations..."
alembic upgrade head

# Lancer l'application
echo "Starting FastAPI application..."
gunicorn App.main:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
