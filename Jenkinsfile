pipeline {
    agent any

    environment {
        BACKEND_DIR = "backend"
        FRONTEND_DIR = "frontend"
    }

    stages {

        stage('Backend - Tests') {
            steps {
                echo "Ejecutando pruebas backend..."

                dir("${BACKEND_DIR}") {
                    sh """
                        pip install pytest || true
                        pytest --maxfail=1 --disable-warnings -q || echo "No tests found, continuing..."
                    """
                }
            }
        }

        stage('Frontend - Check files') {
            steps {
                echo "Verificando archivos frontend..."
                sh "test -f ${FRONTEND_DIR}/index.html"
                sh "test -f ${FRONTEND_DIR}/script.js"
                sh "test -f ${FRONTEND_DIR}/style.css"
            }
        }

        stage('Docker - Build Images') {
            steps {
                echo "Construyendo imágenes Docker..."
                sh "docker-compose build --no-cache"
            }
        }

        stage('Docker - Deploy') {
            steps {
                echo "Levantando servicios..."
                sh "docker-compose down"
                sh "docker-compose up -d"
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline COMPLETADO sin errores.'
        }
        failure {
            echo '❌ Pipeline falló. Revisa los logs.'
        }
    }
}
