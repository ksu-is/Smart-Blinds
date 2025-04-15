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

### During sprint 2, you should be coding and using git to manage your code. 
### Complete these tasks

- [ ] Get Github desktop working.
      
- [ ] Each person should making small updates and adding commit messages with them in your repository in our Github organization so that your work is visible. Do this with Github desktop. Otherwise, it will appear you are not working, and you will fail to demonstrate your knowledge of the application development process, which is one of our course goals. Thus, even if you claim to be working on your own machine but fail to post updates in Github in our shared organization where the professor can see them, you will fail on this grading item.
      
- [ ] Each person should have committed at least 6 code changes of significant size (not just a spelling error fix for example). Each commit should include a comment that explains what you did. The comment must be specific (ie. not just Updated README.md but rather explain what your update was and why you did it briefly).
      
- [ ] You need to be tracking your progress on planned and emerging tasks in your projectroadmap.md document. I will look for changes in this document as signs of your progress. Using checkboxes, adding new tasks as they emerge, or adding “DONE” to mark done items all could count here.

## Sprint 3

### Complete these tasks
      
- [ ] Continue coding and refining and testing in Sprint 3 as in Sprint 2. I will look for additional progress.
- [ ] If you had minor scope for your project and finish already, you need to add more scope and work on it.
- [ ] In addition, coders typically think little about marketing and sustaining their projects. Inside a business there are many stakeholders who are not technical. As project managers and communicators who span the gap between the business and the coders, we need to create ways to communicate our projects quickly and accurately. This is just such an activity. 

- [ ] Create one PowerPoint slide introducing your project and upload it.
- [ ] If you have more than one teammate, each needs to turn-in a copy in D2L to ensure everyone has a copy. The slide needs to be attractive and informative. Be sure to include this information:
- [ ] List your project team members.
- [ ] Show the title of your project.
- [ ] Show a tag line that introduces the main concept of what it does/will do.
- [ ] Show 1-2 screenshots or pictures demonstrating the idea or parts (optional) Each person must upload a PPT slide in D2L. Each team must ensure there is a copy in their Github repository so that future coders can quickly grasp the idea.

## Sprint 4

### Presentation

This presentation mimics real-world application development today in which people solve technical problems together and give tutorials and demos online. One main objective is to get you to present to your peers and demonstrate your capability at using Microsoft Teams for such a purpose (Goal 3).
