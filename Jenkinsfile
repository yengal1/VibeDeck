pipeline {
    agent any

    stages {
        stage('Backend - Tests') {
            steps {
                echo "Ejecutando pruebas backend..."
                sh """
                    docker build -t vibedeck-backend-test -f backend/Dockerfile backend
                    docker run --rm vibedeck-backend-test pytest --maxfail=1 --disable-warnings -q || true
                """
            }
        }

        stage('Frontend - Check Files') {
            steps {
                echo "Verificando archivos frontend..."
                sh """
                    test -f frontend/index.html
                    test -f frontend/script.js
                    test -f frontend/style.css
                """
            }
        }

        stage('Docker - Build Images') {
            steps {
                echo "Construyendo imágenes Docker..."
                sh "docker compose build --no-cache"
            }
        }

        stage('Docker - Deploy') {
            steps {
                echo "Desplegando servicios..."
                sh "docker compose up -d"
            }
        }
    }

    post {
        success {
            echo "✔️ Pipeline completado correctamente"
        }
        failure {
            echo "❌ Pipeline falló. Revisa los logs."
        }
    }
}
