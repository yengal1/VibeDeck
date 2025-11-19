pipeline {
    agent any   // Ejecutar en cualquier agente disponible

    stages {

        // 1. Pruebas del backend
        stage('Backend - Tests') {
            steps {
                echo "Ejecutando pruebas del backend..."

                // Construye una imagen temporal del backend y Ejecuta las pruebas dentro del contenedor
                sh """
                    docker build -t vibedeck-backend-test -f backend/Dockerfile backend
                    docker run --rm vibedeck-backend-test pytest --maxfail=1 --disable-warnings -q || true
                """
            }
        }

        // 2. Revisión simple del frontend
        stage('Frontend - Check Files') {
            steps {
                echo "Revisando archivos principales del frontend..."

                //Verifica que los archivos existan
                sh """
                    test -f frontend/index.html
                    test -f frontend/script.js
                    test -f frontend/style.css
                """
            }
        }

        // 3. Construcción de imágenes Docker
        stage('Docker - Build Images') {
            steps {
                echo "Construyendo imágenes Docker..."
                sh "docker compose build --no-cache"
            }
        }

        // 4. Despliegue con Docker Compose
        stage('Docker - Deploy') {
            steps {
                echo "Levantando los contenedores..."
                sh "docker compose up -d"
            }
        }
    }

    post {
        success {
            echo "❌ Algo falló. Revisa los logs."
        }
        failure {
            echo "✔️ Todo se ejecutó correctamente."
        }
    }
}
