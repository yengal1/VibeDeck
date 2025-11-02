# frontend/Dockerfile

# 1. Imagen base: Nginx versión alpine para un contenedor ligero
# VibeDeck/frontend/Dockerfile
FROM nginx:alpine

# Copiar archivos estáticos de la carpeta local 'frontend' 
# a la carpeta de servicio de Nginx dentro del contenedor.
COPY . /usr/share/nginx/html 

EXPOSE 80
# El comando por defecto de Nginx (CMD) ya está configurado en la imagen base.