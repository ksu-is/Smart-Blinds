from machine import Pin, PWM
import time

servo = PWM(Pin(18))
servo.freq(50)

while True:
    servo.duty_u16(3000)   # ~0°
    time.sleep(1)
    servo.duty_u16(7500)   # ~90°
    time.sleep(1)
    servo.duty_u16(12000)  # ~180°
    time.sleep(1)