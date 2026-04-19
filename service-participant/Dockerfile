FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Option simple pour l'instant (on améliorera avec entrypoint plus tard)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "participant_project.wsgi:application"]