🧭 F5 Taximeter — Proyecto CLI en Python

F5 Taximeter es una aplicación de consola desarrollada en Python que simula el funcionamiento de un taxímetro real.
Permite iniciar un trayecto, calcular tarifas según el estado del taxi y finalizar el viaje mostrando un resumen completo.

Este proyecto forma parte de una práctica de programación por niveles (Esencial → Medio → Avanzado → Experto).



🚦 Nivel Esencial — Funcionalidades implementadas

✔ Mensaje de bienvenida al iniciar el programa
✔ Sistema de comandos básicos (start, stop, move, finish, exit)
✔ Inicio de trayecto con estado inicial parado
✔ Cálculo automático de tarifas:

0.02 €/s cuando el taxi está parado

0.05 €/s cuando el taxi está en movimiento

✔ Finalización del trayecto con:

tiempo parado

tiempo en movimiento

tarifa total

✔ Reset completo para permitir iniciar un nuevo viaje sin cerrar el programa



📌 Uso del programa

Una vez ejecutado, el CLI muestra los comandos disponibles:

start   → Inicia un nuevo trayecto
stop    → Cambia el estado del taxi a detenido
move    → Cambia el estado del taxi a movimiento
finish  → Finaliza el trayecto y muestra el total
exit    → Cierra el programa




Ejemplo:

> start
Trip started. Initial state: 'stopped'.
> move
State changed to 'moving'.
> stop
State changed to 'stopped'.
> finish
--- Trip Summary ---
Stopped time: 12.5 seconds
Moving time: 30.0 seconds
Total fare: €1.79



🗂 Estructura del proyecto
project-taximetro/
│
├── src/
│   └── taximeter.py
│
├── README.md
├── .gitignore
└── requirements.txt (opcional)



🔧 Requisitos

Python 3.8 o superior

No requiere librerías externas



▶️ Cómo ejecutar

En la raíz del proyecto:

python3 src/taximeter.py



🧩 Próximos niveles del proyecto

Los siguientes niveles añadirán:

Nivel Medio → logs, tests, registro histórico

Nivel Avanzado → refactor OOP, autenticación, GUI

Nivel Experto → base de datos, Docker, versión web



👤 Autor

Desarrollado por Raul Machaca 😎 como práctica de programación.