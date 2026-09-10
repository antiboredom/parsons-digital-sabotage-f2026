import random
import time

import pyautogui

screen_width, screen_height = pyautogui.size()

while True:
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    pyautogui.moveTo(x, y)
    time.sleep(0.01)
