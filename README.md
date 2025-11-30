# 🎶 VibeDeck

**Proyecto finalizado**

VibeDeck es una aplicación web sencilla pero funcional enfocada en la **gestión de ambientes digitales de concentración**, combinando colores y música según el estado de ánimo del usuario.

El propósito principal del proyecto es **poner en práctica los conceptos de integración continua, control de versiones y manejo de contenedores con Docker, y el Despliegue Continuo (CD)**.

---

## 💡 Descripción del proyecto

El sistema permitirá que el usuario ingrese un estado de ánimo o concepto (por ejemplo, **"calmado"**) y, mediante una **API**, reciba:
* Una **paleta de color** en formato HEX.
* Una **URL de música** relacionada con ese estado de ánimo.

La estructura modular del proyecto permite su **escalabilidad y mantenimiento**, siguiendo las buenas prácticas del desarrollo moderno.

---

## 🏗️ Arquitectura Final del Sistema

El sistema opera bajo un diseño **Contenerizado de Tres Capas Lógicas**, orquestado por **Docker Compose** (`v3.8`).

| Servicio | Capa de la Arquitectura | Tecnología Utilizada | Acceso Local |
| :--- | :--- | :--- | :--- |
| **`api`** (Backend) | Lógica de Negocio y Datos | **Python (FastAPI)** | `http://localhost:8000` |
| **`web`** (Frontend) | Presentación | **Nginx** | `http://localhost` |
| **Persistencia** | Datos | **SQLite** | **Interna** (Archivo persistido mediante el volumen `db_data`) |

---

## 🧩 Tecnologías y Herramientas CI/CD

Esta fase aplica las siguientes herramientas clave para la automatización:

| Categoría | Herramienta | Uso en el Proyecto |
| :--- | :--- | :--- |
| **Backend** | Python (FastAPI) | Procesamiento de solicitudes y lógica de negocio. |
| **Interfaz** | HTML, CSS, JS Vanilla | Interfaz de usuario servida por Nginx. |
| **Contenerización** | **Docker Compose** | Orquestación y ejecución de los servicios `api` y `web`. |
| **Control de Versiones** | **GitHub** | Control central y **fuente de *triggers*** (webhooks) para el CI/CD. |
| **Integración Continua** | **Jenkins** | Automatización del *pipeline* completo (Test, Build, Deploy), configurado vía `Jenkinsfile`. |
| **Calidad del Código** | **Codecov** | Medición de la **cobertura de pruebas** y aplicación de umbrales de calidad en Pull Requests. |

---

## 🚀 Pipeline CI/CD: Flujo y Ejecución

El proyecto implementa un *pipeline* completamente automatizado con **Jenkins**, activado por eventos en GitHub, validado y funcional (confirmado por PR #3).

1.  **Source:** *Trigger* automático vía **webhook de GitHub**.
2.  **Test & Quality:** Ejecución de pruebas unitarias y **subida del reporte de cobertura a Codecov**.
3.  **Build:** Construcción y etiquetado de las **Imágenes Docker** (`api` y `web`).
4.  **Deploy:** Despliegue de la nueva versión con **cero *downtime*** en el servidor remoto.

### Cómo Ejecutar el Proyecto (Desarrollo Local)

Asegúrate de tener Docker y Docker Compose instalados.


# 1. Clona el repositorio
git clone [https://aws.amazon.com/es/what-is/repo/](https://aws.amazon.com/es/what-is/repo/)
cd VibeDeck

# 2. Construye y levanta los servicios
docker compose up --build

---
#Acceso:

Aplicación (Frontend): http://localhost

API (Acceso directo): http://localhost:8000

---

## 👩‍💻 Integrantes del equipo
- **Yeni Galindo**  
- **Kewin Guzman Diaz** 
- **German David Navas Rodriguez** 

---

## 🏗️ Estado del proyecto
🟢 
FINALIZADO – Entrega Final Implementación y automatización exitosa de la arquitectura contenida y del Pipeline CI/CD con Jenkins y Codecov.

---

## 🧠 Institución
**Politécnico Grancolombiano**  
Módulo: *Integración Continua – Entrega Final*

---
