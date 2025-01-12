# Utilise une image de base Python
FROM python:3.10-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requirements
COPY requirements.txt /app/

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le projet dans le conteneur
COPY . /app/

# Expose le port 8000 pour le serveur de développement
EXPOSE 8000

# Commande par défaut pour exécuter le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
