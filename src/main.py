def taximeter():
    print("Welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    while True:
        command = input("> ").strip().lower()

        if command == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")

if __name__ == "__main__":
    taximeter()
