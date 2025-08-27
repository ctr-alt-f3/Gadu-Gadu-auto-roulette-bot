import pyautogui
import keyboard
print (pyautogui.position())

keyboard.add_hotkey('ctrl + shift + z', print, args =((pyautogui.position())))

keyboard.wait()

