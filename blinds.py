from machine import Pin, PWM
import time

# Store file on Pico (no home directory)
FILENAME = "status.txt"

# Motor timing constants
TIMEUP = 38
TIMEDOWN = 22

# PWM duty values for servo positions (adjust as needed)
UP_FAST = 10000     # ~2ms pulse
DOWN_FAST = 5000    # ~1ms pulse
CENTER = 7500       # ~1.5ms pulse (neutral)

CLOSED = 0
OPENED = 1

class Blinds:
    def __init__(self):
        self.status = 0
        self.read_status()

        # Setup PWM on GPIO 18 at 50Hz
        self.pwm = PWM(Pin(18))
        self.pwm.freq(50)

        # Move to center position to start
        self.pwm.duty_u16(CENTER)

    def read_status(self):
        try:
            with open(FILENAME, "r") as f:
                self.status = float(f.readline().strip())
        except:
            self.status = 0  # Default if file not found

    def write_status(self):
        with open(FILENAME, "w") as f:
            f.write(str(self.status))

    def move(self, target):
        if target > self.status:
            self.pwm.duty_u16(UP_FAST)
            time.sleep(TIMEUP * (target - self.status))
        elif target < self.status:
            self.pwm.duty_u16(DOWN_FAST)
            time.sleep(TIMEDOWN * (self.status - target))

        # Stop servo (reset to center or turn off)
        self.pwm.duty_u16(CENTER)

        self.status = target
        self.write_status()

    def toggle(self):
        if self.status == OPENED:
            self.move(CLOSED)
        elif self.status == CLOSED:
            self.move(OPENED)
        return self.status

# Basic example for testing
if __name__ == "__main__":
    blinds = Blinds()
    blinds.toggle()
