// Crea un volumen para persistir datos de Jenkins
docker volume create jenkins_home

// Ejecuta Jenkins (permite acceso al docker.sock para que Jenkins construya imágenes)
docker run -d \
--name jenkins \
-p 8080:8080 \
-p 50000:50000 \
-v jenkins_home:/var/jenkins_home \
-v /var/run/docker.sock:/var/run/docker.sock \
jenkins/jenkins:lts


// Muestra el password inicial (espera unos segundos a que arranque)
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword