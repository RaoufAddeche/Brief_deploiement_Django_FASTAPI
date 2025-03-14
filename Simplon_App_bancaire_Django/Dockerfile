FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app


# Copier et exécuter le script d'installation des drivers SQL Server
COPY install_sql_driver.sh install_sql_driver.sh
RUN chmod +x ./install_sql_driver.sh && ./install_sql_driver.sh

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Change to the directory containing manage.py
WORKDIR /app/Bamk

# Expose port 8080
EXPOSE 8080

# Run Gunicorn using the WSGI module in the inner Bamk folder
CMD ["gunicorn", "Bamk.wsgi:application", "-w","3", "--bind", "0.0.0.0:8080"]
