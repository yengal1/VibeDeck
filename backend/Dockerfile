# VibeDeck/backend/Dockerfile
FROM python:3.10-slim

# 1. Establecer el directorio de trabajo
WORKDIR /app

# 2. Copiar el requirements.txt
COPY requirements.txt .

# 3. CLAVE: Forzar la actualización de PIP y la instalación en un solo paso
# Esto garantiza que todos los módulos y sus binarios (como uvicorn) se instalen correctamente.
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
COPY ./app /app/app

# 5. Comando de inicio corregido
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]