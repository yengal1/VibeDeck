# backend/Dockerfile

# 1. Imagen base: Python 3.10 versión slim para reducir tamaño
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo
WORKDIR /app

# 3. Copiar e instalar dependencias (aprovechando el cache de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
# (Copiamos el contenido de la carpeta local ./app a /app/app en el contenedor)
COPY ./app /app/app

# 5. Comando de inicio: Ejecutar la aplicación FastAPI
# Uvicorn ejecutará el objeto 'app' que se encuentra en 'app/main.py'
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]