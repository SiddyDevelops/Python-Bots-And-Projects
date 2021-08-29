import pyautogui as pt
from time import sleep

# https://mouseaccuracy.com/

pt.FAILSAFE = True

def nav_to_image(image, click):
    try:
        position = pt.locateCenterOnScreen(image, confidence=0.8)
        pt.moveTo(position,duration=0.001)
        pt.click(clicks=click,interval=0.1)
    except Exception as e:
        print(f'{image} not found...',e)

sleep(2)
nav_to_image('Images\image1.PNG',2)    
sleep(3)

for i in range(50):
    nav_to_image("Images\circle.PNG",1)



        