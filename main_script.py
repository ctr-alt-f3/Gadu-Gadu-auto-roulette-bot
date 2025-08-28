import pyautogui
import pyperclip
from time import sleep
from pynput import keyboard
from sys import exit
import GG2prof 
import random 
import keyboard 

keyboard.add_hotkey('shift + z', exit,args = ())
keyboard.add_hotkey('shift + z', print,args = ("exit"))
# keyboard.add_hotkey('shift + z', print(),args = (0/0))
keyboard.wait('esc') 

def schowaj():
    with open("linki.txt","a") as file:
        pyautogui.rightClick(1427, 465)
        sleep(0.2)
        pyautogui.click(1582, 650)
        link = pyperclip.paste()
        parsing = link.split('/')
        GGnumber = parsing[-1]
        GG2prof.GG2prof(GGnumber,GGnumber) 
        file.write(link)
        file.write("\n")


while True:
    # pyautogui.hotkey('ctrl', 'tab')

    try:
        losuj_dalej = pyautogui.locateCenterOnScreen('losuj_dalej.png', confidence=0.7)
        sleep(0.5)
        if losuj_dalej:
            sleep(1)
            print("chowam")
            schowaj()
            pyautogui.click((losuj_dalej[0]+random.randint(-5, 5)),losuj_dalej[1])
            
            # pyautogui.click(643, 207,button="right")
            

            
        niebieskie_losuj = pyautogui.locateCenterOnScreen('niebieskie_losuj.png', confidence=0.7)
        sleep(0.5)
        if(niebieskie_losuj):
            sleep(0.5)
            pyautogui.click(niebieskie_losuj[0]+random.randint(-5, 5),niebieskie_losuj[1])
            
       
    except:
        pass
    pyautogui.hotkey('ctrl', 'tab')



