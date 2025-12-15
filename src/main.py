import tkinter as tk
from tkinter import messagebox, simpledialog
from src.auth import authenticate
from taximeter import Trip
from src.logger import setup_logger

logger = setup_logger()

# ========================
# AUTENTICACIÓN
# ========================
def login():
    user = simpledialog.askstring("Login", "Username:")
    pwd = simpledialog.askstring("Login", "Password:", show="*")
    if authenticate(user, pwd):
        logger.info(f"User '{user}' logged in successfully")
        return True
    else:
        logger.warning(f"Failed login attempt for user '{user}'")
        messagebox.showerror("Error", "Invalid credentials")
        return False

# ========================
# GUI PRINCIPAL
# ========================
class TaximeterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("F5 Taximeter GUI")
        self.trip = Trip()

        # Botones
        self.start_btn = tk.Button(root, text="Start Trip", command=self.start_trip)
        self.start_btn.pack(pady=5)

        self.stop_btn = tk.Button(root, text="Stop", command=lambda: self.change_state("stopped"))
        self.stop_btn.pack(pady=5)

        self.move_btn = tk.Button(root, text="Move", command=lambda: self.change_state("moving"))
        self.move_btn.pack(pady=5)

        self.finish_btn = tk.Button(root, text="Finish Trip", command=self.finish_trip)
        self.finish_btn.pack(pady=5)

        self.fare_label = tk.Label(root, text="Fare: €0.00")
        self.fare_label.pack(pady=5)

    def start_trip(self):
        if self.trip.active:
            messagebox.showwarning("Warning", "Trip already in progress")
            return
        self.trip.start()
        messagebox.showinfo("Info", "Trip started (stopped)")

    def change_state(self, state):
        if not self.trip.active:
            messagebox.showwarning("Warning", "No active trip")
            return
        self.trip.change_state(state)
        messagebox.showinfo("Info", f"State changed to {state}")

    def finish_trip(self):
        if not self.trip.active:
            messagebox.showwarning("Warning", "No active trip")
            return
        total = self.trip.finish()
        self.fare_label.config(text=f"Fare: €{total:.2f}")
        messagebox.showinfo("Trip finished", f"Total fare: €{total:.2f}")

# ========================
# INICIO DEL PROGRAMA
# ========================
if __name__ == "__main__":
    root = tk.Tk()
    if login():
        app = TaximeterGUI(root)
        root.mainloop()
