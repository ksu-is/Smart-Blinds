# Roadmap

## Sprint 1

## Repos
- [x] Get 1 inspired repo from Gtihub - Joe  
- [x] Get 1 inspired repo from Github - William

- [Smart-Blinds/brizdotdev](https://github.com/brizdotdev/Smart-Blinds)  
- [automatic-roller-blinds-motor/asafteirobert](https://github.com/asafteirobert/automatic-roller-blinds-motor)

## Hardware
- [x] find out what hardware brizdotdev is using - Joe
- [ ] find out what hardware asafteirobert is using - William  
### (Smart-Blinds/brizdotdev)
- Raspberry Pi Model 3
- 4x AA Batteries
- Continuous Rotation Servo (SM-4303r) - (This will spin the wand to open and close the blinds)
- [3D Printed gear](http://www.thingiverse.com/thing:867) - (This is intended for "roller blinds", we will not be using these)

### (automatic-roller-blinds-motor/asafteirobert)

## Software  
- [x] find out what software brizdotdev is using - Joe
- [x] find out what software asafteirobert is using - William

### (Smart-Blinds/brizdotdev)
- [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) - "Your Raspberry Pi needs an operating system to work. This is it. Raspberry Pi OS (previously called Raspbian) is our official supported operating system."


### (automatic-roller-blinds-motor/asafteirobert)

## Errors: 
- [x] Clone, test, and document any setup or issues with brizdotdev's code - Joe
- [ ] Clone, test, and document any setup or issues asafteirobert's code - William

(Smart-Blinds/brizdotdev):  
Traceback (most recent call last):  
  File "c:\Users\Joe\Documents\GitHub\Smart-Blinds Insparation\brizdotdevSmart-Blinds\Smart-Blinds\blinds.py", line 4, in <module>  
    import RPi.GPIO as GPIO  
ModuleNotFoundError: No module named 'RPi'

### (automatic-roller-blinds-motor/asafteirobert):

## Possible Error cause:  
### (Smart-Blinds/brizdotdev) 
It’s trying to import RPi.GPIO, which is only available on Raspberry Pi hardware.

### (automatic-roller-blinds-motor/asafteirobert)

## Possible Error fix:  
### (Smart-Blinds/brizdotdev)
import RPi.GPIO as GPIO

### (automatic-roller-blinds-motor/asafteirobert)



## Sprint 2

## Sprint 3

## Sprint 4
