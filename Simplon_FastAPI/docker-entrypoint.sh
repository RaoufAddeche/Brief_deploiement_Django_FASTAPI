#!/bin/bash
set -e

# Afficher les variables d'environnement (en masquant les valeurs sensibles)
echo "Checking environment variables..."
echo "DATABASE_URL is set: ${DATABASE_URL:+true}"
echo "SECRET_KEY is set: ${SECRET_KEY:+true}"
echo "MODEL_PATH is set: ${MODEL_PATH:+true}"

# Attendre que la base de données soit prête
echo "Waiting for database..."
python -c "
import time
import sqlalchemy
import os
import sys

db_url = os.getenv('DATABASE_URL')
max_retries = 30
retry_interval = 3

for i in range(max_retries):
    try:
        engine = sqlalchemy.create_engine(db_url)
        engine.connect()
        print('Database connection successful!')
        sys.exit(0)
    except Exception as e:
        print(f'Attempt {i+1}/{max_retries}: Database not ready yet... ({str(e)})')
        time.sleep(retry_interval)

print('Could not connect to database after maximum retries')
sys.exit(1)
"

# Appliquer les migrations Alembic
# echo "Applying database migrations..."
# alembic upgrade head

# Lancer l'application avec Gunicorn
echo "Starting FastAPI application..."
exec gunicorn App.main:app \
    --worker-class uvicorn.workers.UvicornWorker \
    --workers 4 \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --keep-alive 5 \
    --log-level debug \
    --access-logfile - \
    --error-logfile - \
    --capture-output \
    --enable-stdio-inheritance