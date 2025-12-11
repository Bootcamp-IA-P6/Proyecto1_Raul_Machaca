import time
from logger import logger     # <--- NUEVO IMPORT

def calculate_fare(seconds_stopped, seconds_moving):
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    logger.info(f"Cálculo de tarifa: stopped={seconds_stopped}, moving={seconds_moving}, total={fare}")
    return fare

def taximeter():
    logger.info("Programa iniciado")
    print("Welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_active = False
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()
        logger.info(f"Comando recibido: {command}")

        if command == "start":
            if trip_active:
                print("Error: A trip is already in progress.")
                logger.warning("Intento de iniciar un viaje ya activo")
                continue

            trip_active = True
            stopped_time = 0
            moving_time = 0
            state = "stopped"
            state_start_time = time.time()

            logger.info("Viaje iniciado")
            print("Trip started. Initial state: 'stopped'.")

        elif command in ("stop", "move"):
            if not trip_active:
                print("Error: No active trip. Please start first.")
                logger.warning("Comando stop/move sin viaje activo")
                continue

            duration = time.time() - state_start_time
            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration

            state = "stopped" if command == "stop" else "moving"
            state_start_time = time.time()

            logger.info(f"Estado cambiado a {state}")
            print(f"State changed to '{state}'.")

        elif command == "finish":
            if not trip_active:
                print("Error: No active trip to finish.")
                logger.warning("Intento de finalizar sin viaje")
                continue

            duration = time.time() - state_start_time
            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration

            total_fare = calculate_fare(stopped_time, moving_time)

            print("\n--- Trip Summary ---")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")

            logger.info(f"Viaje finalizado. Total={total_fare}")

            trip_active = False
            state = None

        elif command == "exit":
            logger.info("Programa cerrado por el usuario")
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Unknown command.")
            logger.warning(f"Comando desconocido: {command}")
