# Image de base : Python léger (moins volumineux qu'une image Python complète)
FROM python:3.11-slim

# Dossier de travail à l'intérieur du container
WORKDIR /app

# On copie d'abord uniquement requirements.txt
# (astuce : Docker met en cache cette étape tant que ce fichier ne change pas,
# donc les rebuilds sont plus rapides si tu modifies juste ton code)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Maintenant on copie le reste du code
COPY . .

# Port sur lequel l'API va écouter à l'intérieur du container
EXPOSE 8005

# Commande lancée au démarrage du container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]