from machine import Pin
import time

FILENAME = "status.txt"

MOTOR_PIN = 16         # GPIO pin controlling the transistor
RUN_TIME = 4           # Total time in seconds to fully open or close

CLOSED = 0
OPENED = 1

class Blinds:
    def __init__(self):
        self.status = CLOSED
        self.read_status()

        self.motor = Pin(MOTOR_PIN, Pin.OUT)
        self.motor.value(0)

    def read_status(self):
        try:
            with open(FILENAME, "r") as f:
                self.status = int(float(f.readline().strip()))
                print(f"Status read from file: {self.status}")
        except:
            self.status = CLOSED
            print("No status file found. Defaulting to CLOSED.")

    def write_status(self):
        with open(FILENAME, "w") as f:
            f.write(str(self.status))
        print(f"Status written: {self.status}")

    def move(self, target):
        if target == self.status:
            print("Blinds already in desired position.")
            return

        print("Moving motor with pulses...")
        pulse_count = int(RUN_TIME * 10)  # 10 pulses per second
        for _ in range(pulse_count):
            self.motor.value(1)
            time.sleep(0.1)  # ON duration
            self.motor.value(0)
            time.sleep(0.05)  # OFF duration

        print("Motor pulsing complete.")
        self.status = target
        self.write_status()

    def toggle(self):
        print("Toggling blinds...")
        if self.status == OPENED:
            self.move(CLOSED)
        else:
            self.move(OPENED)
        return self.status