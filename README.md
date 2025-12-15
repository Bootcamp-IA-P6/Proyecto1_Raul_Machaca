Project Taxímetro - Nivel Avanzado

Este proyecto simula un taxímetro en Python, incorporando programación orientada a objetos (OOP), una interfaz gráfica (GUI), autenticación de usuario y sistema de logs para llevar un historial de los viajes.




Funcionalidades

Iniciar y finalizar trayectos, controlando:

Tiempo parado

Tiempo en movimiento

Cálculo automático del precio según tarifas configurables

Registro histórico de trayectos (logs/trips_history.txt)

Sistema de logs para trazabilidad (logs/taximeter.log)

Autenticación con usuario y contraseña

Interfaz gráfica con botones para manejar el viaje

Código organizado en OOP

Tests unitarios para funciones clave y la clase Trip



Configuración

El archivo config.py permite ajustar parámetros como tarifas y credenciales:

STOPPED_RATE = 0.02   # €/segundo parado
MOVING_RATE = 0.05    # €/segundo en movimiento

USERNAME = "admin"
PASSWORD = "1234"     # Para proyectos reales, usar hashing



Cómo ejecutar

Desde la raíz del proyecto, ejecuta:

python -m src.main


Se abrirá una ventana de login. Ingresa el usuario y contraseña definidos en config.py.

La GUI tiene los siguientes botones:

Start Trip → Inicia el viaje (estado inicial: parado)

Move → Cambia a estado en movimiento

Stop → Cambia a estado parado

Finish Trip → Termina el viaje, calcula la tarifa y guarda el historial




Historial de trayectos

Cada viaje se guarda en logs/trips_history.txt con este formato:

Stopped: 10.0s | Moving: 20.0s | Total: €1.40




Los eventos y acciones también se registran en logs/taximeter.log.

Tests unitarios

Para probar las funciones de cálculo y la clase Trip:

python -m pytest



Requisitos

Python 3.7 o superior

Tkinter (normalmente incluido en Python)

pytest (solo para tests)




Estructura del proyecto
project-taximetro/
│
├── logs/
│   └── taximeter.log
│
├── src/
│   ├── logger.py
│   ├── main.py
│   └── auth.py
│
├── tests/
│   └── test_taximeter.py
│
├── taximeter.py
├── config.py
├── README.md
└── .gitignore