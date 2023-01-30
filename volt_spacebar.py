import time
import sys
import keyboard
import pandas as pd
from PIL import ImageGrab
import matplotlib.pylab as plt
from glob import glob
from pynput.keyboard import Key, Controller
import pyautogui

print(pyautogui.size())


# Rests the lock
pyautogui.moveTo(352, 16, duration=1)
pyautogui.click(352, 16)
pyautogui.typewrite(' ')
pyautogui.typewrite(' ')
pyautogui.typewrite(' ')
pyautogui.typewrite(' ')
time.sleep(float(2.1))

# Gets 3
time.sleep(float(2))
pyautogui.typewrite(' ')

# Gets 9
time.sleep(float(2))
pyautogui.typewrite(' ')

# Gets 5
time.sleep(float(3))
pyautogui.typewrite(' ')

# Gets 0
time.sleep(float(1.3))
pyautogui.typewrite(' ')

# Gets 2
time.sleep(float(1))
pyautogui.typewrite(' ')

# LOCK ONE OVER

# Gets 8
time.sleep(float(3.5))
pyautogui.typewrite(' ')

# Gets 4
time.sleep(float(3))
pyautogui.typewrite(' ')

# Gets 7
time.sleep(float(2.2))
pyautogui.typewrite(' ')

# Gets 1
time.sleep(float(1.5))
pyautogui.typewrite(' ')

# Gets 6
time.sleep(float(1))
pyautogui.typewrite(' ')

# LOCK TWO OVER

# Gets 2
time.sleep(float(4))
pyautogui.typewrite(' ')

# Gets 6
time.sleep(float(4.2))
pyautogui.typewrite(' ')

# Gets 4
time.sleep(float(1.55))
pyautogui.typewrite(' ')

# Gets 9
time.sleep(float(1.5))
pyautogui.typewrite(' ')

# Gets 5
time.sleep(float(1))
pyautogui.typewrite(' ')

# LOCK THREE OVER

# Gets 0
time.sleep(float(4.09 ))
pyautogui.typewrite(' ')

# Gets 1
time.sleep(float(1.33))
pyautogui.typewrite(' ')

# Gets 8
time.sleep(float(2.183))
pyautogui.typewrite(' ')

# Gets 3
time.sleep(float(5.5))
pyautogui.typewrite(' ')

# Gets 6
time.sleep(float(6.2 ))
pyautogui.typewrite(' ')

print("lock has been reset.")

#pyautogui.moveTo(-266, -257, duration=1)
#pyautogui.click(-266, -257)

lock = 4
key_digit = 5
time = 0

arr = [[time] * key_digit] * lock
#for i in lock:
 #   for j in key_digit:
       # array[]
print(arr)