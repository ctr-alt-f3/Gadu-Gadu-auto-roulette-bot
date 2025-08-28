import pyautogui
import keyboard
import pyperclip
from time import sleep 
# sleep(3) 
# pyautogui.rightClick(x=968, y=299)
def schowaj():
    print(pyperclip.paste())
    # with open("linki.txt","a") as file:
        # file.write(pyperclip.paste())
        # file.write("\n")
keyboard.add_hotkey('shift + z', pyautogui.rightClick, args = (1421, 469))
keyboard.add_hotkey('shift + x', pyautogui.click, args = (1599, 652))
keyboard.add_hotkey('shift + c', schowaj, args = ())





keyboard.wait()