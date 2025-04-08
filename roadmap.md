# Roadmap

## Sprint 1

### Repos
- [x] Get 1 inspired repo From Gtihub - Joe

- [Smart-Blinds/brizdotdev](https://github.com/brizdotdev/Smart-Blinds)

### Hardware
- [x] find out what hardware brizdotdev is using - Joe

- Raspberry Pi Model 3
- 4x AA Batteries
- Continuous Rotation Servo (SM-4303r)
- This will spin the wand to open and close the blinds
- [3D Printed gear](http://www.thingiverse.com/thing:867)
- This is intended for "roller blinds", we will not be using these

### Software
- [x] find out what software brizdotdev is using - Joe

- [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
-"Your Raspberry Pi needs an operating system to work. This is it. Raspberry Pi OS (previously called Raspbian) is our official supported operating system."

### Errors:
- [x] Clone, test, and document any setup or issues with brizdotdev's code

Traceback (most recent call last):
  File "c:\Users\Joe\Documents\GitHub\Smart-Blinds Insparation\brizdotdevSmart-Blinds\Smart-Blinds\blinds.py", line 4, in <module>
    import RPi.GPIO as GPIO
ModuleNotFoundError: No module named 'RPi'

### Possible Error cause:
It’s trying to import RPi.GPIO, which is only available on Raspberry Pi hardware.

### Possible Error fix:
import RPi.GPIO as GPIO


## Sprint 2

## Sprint 3

## Sprint 4
