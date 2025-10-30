# frontend/Dockerfile

# 1. Imagen base: Nginx versión alpine para un contenedor ligero
FROM nginx:alpine

# 2. Copiar los archivos estáticos HTML, CSS, JS 
# Al destino por defecto de los archivos servidos por Nginx
COPY . /usr/share/nginx/html

# 3. Exponer el puerto por defecto de Nginx
EXPOSE 80

# El comando por defecto de Nginx (CMD) ya está configurado en la imagen base.