import time

def taximeter():
    print("Welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()

        if command == "start":
            if trip_active:
                print("Error: A trip is already in progress.")
                continue
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'
            state_start_time = time.time()
            print("Trip started. Initial state: 'stopped'.")

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")

if __name__ == "__main__":
    taximeter()
