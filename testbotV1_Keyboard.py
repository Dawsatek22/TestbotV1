import pygame
from time import sleep
from adafruit_servokit import ServoKit

slegl1 = 1 #the first left  leg
slegl2 = 0 # second left leg
slegr1 = 15 first right leg
slegr2 = 14 second right leg


kit = ServoKit(channels=16)
pygame.init()
window = pygame.display.set_mode((300,300))
pygame.display.set_caption("Pygame Demonstration")
def calibration(): # this calibrates the servo to 90 degrees
    kit.servo[slegr1].angle = 90
    kit.servo[slegr2].angle = 90
    kit.servo[slegl1].angle = 90
    kit.servo[slegl2].angle = 90
   

    
    

mainloop=True
while mainloop:

    pygame.time.delay(100)
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            mainloop=False

        pressed = pygame.key.get_pressed()
        buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
        print(buttons)  # print list to console
        if pressed[pygame.K_c]: #calibrates if the c button on the keyboard is pressed.
            calibration()
            print("calibration")
           
        
        if pressed[pygame.K_f]:
               kit.servo[slegr1].angle = 180
               kit.servo[slegr2].angle = 180
               kit.servo[slegl1].angle = 0
               kit.servo[slegl2].angle = 0
               sleep(0.5)
               kit.servo[slegr1].angle = 90
               kit.servo[slegr2].angle = 90
               kit.servo[slegl1].angle = 90
               kit.servo[slegl2].angle = 90
               print("Forward") #tries to move forward when f button is pushed
       
                

pygame.quit()

