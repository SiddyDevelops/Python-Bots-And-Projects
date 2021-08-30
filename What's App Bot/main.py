from os import close
import pyautogui as pt
from pynput import mouse
import pyperclip as pc
from pynput.mouse import Button, Controller
from time import sleep

pt.FAILSAFE = True
mouse = Controller()

# NAv to image 
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.8)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=3)
        pt.moveRel(off_x, off_y, duration=0.2)
        pt.click(clicks=clicks, interval=0.1)


def get_message():
    nav_to_image('images\clip.PNG',clicks=0,off_x=30,off_y=-90)
    mouse.click(Button.left, 3)
    pt.rightClick()

    copy = nav_to_image('images\copy_window.PNG',clicks=1)
    sleep(0.5)
    return pc.paste() if copy !=0 else 0 

def send_message(msg):
    nav_to_image('images\clip.PNG',clicks=2, off_x=100)
    pt.typewrite(msg, interval=0.1)
    # pt.typewrite('\n')

def close_reply_box():
    nav_to_image('images\close.PNG',clicks=2)

def process_message(msg):
    raw_message = msg.lower()

    if raw_message == 'Hello':
        return 'Hey there!'
    elif raw_message == 'Yes':
        return 'Bot says you said yes!'
    elif 'ok' in raw_message:
        return 'You wrote Ok!'
    else:
        return 'I did not understand what you wrote.'  

                              

sleep(3)   

# nav_to_image(r'images\unread.PNG', clicks=0) 
# nav_to_image('images\copy_window.PNG',clicks=0)            
# nav_to_image('images\close.PNG',clicks=0)            
# nav_to_image('images\clip.PNG',clicks=0)
        
# Loop the code
delay = 10  #secs
last_message = ''

while True:
    #Checks for new messages 
    nav_to_image(r'images\unread.PNG', clicks=2, off_x=-100)  #1
    close_reply_box() #2

    message = get_message() #3
    if message != 0 and message != last_message:
        last_message = message
        send_message(process_message(message))
    else:
        print('No new messages...')

    sleep(5)        
