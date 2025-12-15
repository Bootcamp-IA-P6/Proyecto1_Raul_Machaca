import time
from src.logger import setup_logger

# ========================
# CONFIGURACIÓN DE TARIFAS
# ========================
STOPPED_RATE = 0.02   # €/segundo parado
MOVING_RATE = 0.05    # €/segundo en movimiento

logger = setup_logger()

# ========================
# FUNCIONES
# ========================
def calculate_fare(seconds_stopped, seconds_moving):
    fare = seconds_stopped * STOPPED_RATE + seconds_moving * MOVING_RATE
    return fare


def save_trip(stopped_time, moving_time, total_fare):
    with open("logs/trips_history.txt", "a") as file:
        file.write(
            f"Stopped: {stopped_time:.1f}s | "
            f"Moving: {moving_time:.1f}s | "
            f"Total: €{total_fare:.2f}\n"
        )


def taximeter():
    print("🚕 Welcome to the F5 Taximeter!")
    print("Commands: start | stop | move | finish | exit\n")

    logger.info("Taximeter program started")

    trip_active = False
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()

        if command == "start":
            if trip_active:
                print("❌ Trip already in progress.")
                logger.warning("Attempt to start a trip while another is active")
                continue

            trip_active = True
            stopped_time = 0
            moving_time = 0
            state = "stopped"
            state_start_time = time.time()

            print("✅ Trip started. State: stopped.")
            logger.info("Trip started")

        elif command in ("stop", "move"):
            if not trip_active:
                print("❌ No active trip.")
                logger.warning("State change without active trip")
                continue

            duration = time.time() - state_start_time

            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration

            state = "stopped" if command == "stop" else "moving"
            state_start_time = time.time()

            print(f"🔄 State changed to {state}")
            logger.info(f"State changed to {state}")

        elif command == "finish":
            if not trip_active:
                print("❌ No active trip to finish.")
                logger.warning("Finish command without active trip")
                continue

            duration = time.time() - state_start_time
            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration

            total_fare = calculate_fare(stopped_time, moving_time)
            save_trip(stopped_time, moving_time, total_fare)

            print("\n📊 Trip Summary")
            print(f"Stopped time: {stopped_time:.1f}s")
            print(f"Moving time: {moving_time:.1f}s")
            print(f"Total fare: €{total_fare:.2f}")
            print("------------------\n")

            logger.info(
                f"Trip finished | Stopped: {stopped_time:.1f}s | "
                f"Moving: {moving_time:.1f}s | Fare: €{total_fare:.2f}"
            )

            trip_active = False
            print("Ready for a new trip 🚕")

        elif command == "exit":
            logger.info("Program exited by user")
            print("👋 Goodbye!")
            break

        else:
            print("❓ Unknown command.")
            logger.warning(f"Unknown command: {command}")


if __name__ == "__main__":
    taximeter()
