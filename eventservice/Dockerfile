FROM python:3.11-slim

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le code Django
COPY . .

EXPOSE 8000

# Lancement du serveur (0.0.0.0 obligatoire pour Kubernetes)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]