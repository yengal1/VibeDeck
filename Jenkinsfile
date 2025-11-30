pipeline {
  // Define en qué tipo de agente se ejecutará el pipeline.
  // 'any' significa que Jenkins usará cualquier nodo disponible.
  agent any

  // Variables de entorno disponibles durante todo el pipeline
  environment {
    IMAGE_TAG = "${env.BUILD_NUMBER}"  // Cada build tendrá un tag único usando el número de build
    ARTIFACT_DIR = "image-artifacts"   // Carpeta donde se guardarán las imágenes Docker como artifacts
  }

  // Opciones generales del pipeline
  options {
    timeout(time: 30, unit: 'MINUTES') // Limita la ejecución total del pipeline a 30 minutos
  }

  stages {
    // Etapa 1: Preparar el espacio de trabajo
    stage('Prepare workspace') {
      steps {
        echo "Preparando carpeta de artifacts..."
        sh '''
          # Borra la carpeta de artifacts anterior si existe
          rm -rf ${ARTIFACT_DIR} || true
          # Crea la carpeta para almacenar los nuevos artifacts
          mkdir -p ${ARTIFACT_DIR}
        '''
      }
    }

    // Etapa 2: Construir la imagen Docker del backend
    stage('Build backend image') {
      steps {
        echo "Construyendo imagen backend: vibedeck/backend:${IMAGE_TAG}"
        sh '''
          # Salir si hay errores, variables no definidas o fallas en pipes
          set -euo pipefail
          # Construye la imagen Docker usando el Dockerfile de backend
          docker build -t vibedeck/backend:${IMAGE_TAG} -f backend/Dockerfile backend
        '''
      }
    }

    // Etapa 3: Construir la imagen Docker del frontend
    stage('Build frontend image') {
      steps {
        echo "Construyendo imagen frontend: vibedeck/frontend:${IMAGE_TAG}"
        sh '''
          set -euo pipefail
          # Construye la imagen Docker usando el Dockerfile de frontend
          docker build -t vibedeck/frontend:${IMAGE_TAG} -f frontend/Dockerfile frontend
        '''
      }
    }

    // Etapa 4: Guardar las imágenes como artifacts para descargarlas o desplegarlas
    stage('Save images as artifacts') {
      steps {
        echo "Guardando imágenes en ${ARTIFACT_DIR}/ ..."
        sh '''
          set -euo pipefail
          # Guarda la imagen de backend en un archivo .tar
          docker save vibedeck/backend:${IMAGE_TAG} -o ${ARTIFACT_DIR}/vibedeck-backend_${IMAGE_TAG}.tar
          # Guarda la imagen de frontend en un archivo .tar
          docker save vibedeck/frontend:${IMAGE_TAG} -o ${ARTIFACT_DIR}/vibedeck-frontend_${IMAGE_TAG}.tar
          # Lista los archivos generados
          ls -lh ${ARTIFACT_DIR}
        '''
      }
    }
  }

  // Acciones que se ejecutan después de que todas las etapas terminan
  post {
    // Si el pipeline termina correctamente
    success {
      echo "✔️ Empaquetado completado. Descarga los artifacts."
    }
    // Si alguna etapa falla
    failure {
      echo "❌ El pipeline falló. Revisa los logs."
    }
    // Siempre se ejecuta, guarde los artifacts generados
    always {
      archiveArtifacts artifacts: "${ARTIFACT_DIR}/*.tar", fingerprint: true
    }
  }
}
