import pyautogui
import keyboard
print (pyautogui.position())
# while True:
keyboard.add_hotkey('ctrl + shift + z', print, args =((pyautogui.position())))

keyboard.wait()
# keyboard.wait('esc') 