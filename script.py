import pyautogui
import pyperclip
from time import sleep
from pynput import keyboard
from sys import exit

sleep(2)
import keyboard 

keyboard.add_hotkey('shift + z', exit,args = ())
keyboard.add_hotkey('shift + z', print,args = ("exit"))

keyboard.wait('esc') 

def hide():
    with open("links.txt","a") as file:
        pyautogui.rightClick(1421, 469)
        pyautogui.click(1599, 652)
        file.write(pyperclip.paste())
        file.write("\n")


while True:


    try:
        losuj_dalej = pyautogui.locateCenterOnScreen('losuj_dalej.png', confidence=0.7)
        sleep(0.5)
        if losuj_dalej:
            sleep(1)
            hide()
            pyautogui.click(losuj_dalej)
            
            # pyautogui.click(643, 207,button="right")
            

            
        niebieskie_losuj = pyautogui.locateCenterOnScreen('niebieskie_losuj.png', confidence=0.7)
        sleep(0.5)
        if(niebieskie_losuj):
            sleep(1)
            pyautogui.click(niebieskie_losuj)
            
       
    except:
        pass
    pyautogui.hotkey('ctrl', 'tab')



