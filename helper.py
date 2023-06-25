import platform
import os
import ctypes
import keyboard

def lock_workstation():
    plt = platform.system()
    if plt == "Linux":
        command = "xdg-screensaver lock"
        os.system(command)
    elif plt=="Windows":
        ctypes.windll.user32.LockWorkStation()
    elif plt == "Darwin":
        keyboard.press_and_release("Command", "L")
    else:
        return