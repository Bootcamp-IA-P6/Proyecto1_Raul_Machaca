📄 README.md (actualizado)
# 🚕 F5 Taximeter - Nivel Experto

Simulación de un taxímetro avanzado en Python con versión web, base de datos y Docker.

## Descripción

Esta aplicación permite simular trayectos de taxi con:

- Control de tiempo parado y en movimiento
- Cálculo de tarifas configurables
- Registro histórico de trayectos en **Supabase**
- Sistema de logs para trazabilidad
- Autenticación de usuario
- Interfaz web con **Streamlit**
- Contenedor Docker para despliegue fácil y portátil

## Estructura del proyecto


Estructura del proyecto
project-taximetro/
│
├── logs/
│   └── taximeter.log
│
├── src/
│   ├── logger.py
│   ├── main.py
│   ├── auth.py
│   └── db.py
│
├── web/ # Versión web con Streamlit
│ └── app.py
│
├── tests/
│   └── test_taximeter.py
│
├── taximeter.py
├── config.py # Configuración tarifas, credenciales y Supabase
├── Dockerfile # Contenedor Docker
├── README.md
├── requirements.txt # Dependencias
└── .gitignore

## Requisitos

- Python 3.10+
- Streamlit
- Supabase
- Docker Desktop (para ejecución en contenedor)

## Instalación y ejecución

### 1️⃣ Clonar proyecto
```bash
git clone <tu-repo-url>
cd project-taximetro

2️⃣ Opción local (sin Docker)
python -m venv venv
venv\Scripts\activate       # Windows
pip install --upgrade pip
pip install -r requirements.txt
streamlit run web/app.py

3️⃣ Opción con Docker
docker build -t taximeter-web .
docker run -p 8501:8501 taximeter-web


Luego abrir navegador en http://localhost:8501

Uso

Ingresar usuario y contraseña (por defecto admin / 1234)

Iniciar trayecto → Start Trip

Cambiar estado → Stop / Move

Finalizar trayecto → Finish Trip

Consultar historial de trayectos desde la base de datos

Tests
python -m pytest


