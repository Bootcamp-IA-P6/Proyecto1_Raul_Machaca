import time
from src.logger import setup_logger
from config import STOPPED_RATE, MOVING_RATE
from src.db import save_trip_to_db

logger = setup_logger()

class Trip:
    def __init__(self):
        self.stopped_time = 0
        self.moving_time = 0
        self.state = None
        self.state_start_time = None
        self.active = False

    def start(self):
        self.active = True
        self.stopped_time = 0
        self.moving_time = 0
        self.state = "stopped"
        self.state_start_time = time.time()
        logger.info("Trip started")

    def change_state(self, new_state):
        if not self.active:
            logger.warning("State change without active trip")
            return
        duration = time.time() - self.state_start_time
        if self.state == "stopped":
            self.stopped_time += duration
        else:
            self.moving_time += duration
        self.state = new_state
        self.state_start_time = time.time()
        logger.info(f"State changed to {self.state}")

    def finish(self):
        if not self.active:
            logger.warning("Finish command without active trip")
            return 0
        duration = time.time() - self.state_start_time
        if self.state == "stopped":
            self.stopped_time += duration
        else:
            self.moving_time += duration
        total_fare = self.calculate_fare()
        save_trip_to_db(self.stopped_time, self.moving_time, total_fare)
        logger.info(f"Trip finished | Stopped: {self.stopped_time:.1f}s | Moving: {self.moving_time:.1f}s | Fare: €{total_fare:.2f}")
        self.active = False
        return total_fare

    def calculate_fare(self):
        return self.stopped_time * STOPPED_RATE + self.moving_time * MOVING_RATE
