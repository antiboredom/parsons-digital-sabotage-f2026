import pyautogui

# get screen width and height
screen_width, screen_height = pyautogui.size()

# get current mouse position
currentMouseX, currentMouseY = pyautogui.position()

# Move the mouse to the x, y coordinates 100, 150.
pyautogui.moveTo(100, 150)

# Click the mouse at its current location.
pyautogui.click()

# Click the mouse at the x, y coordinates 200, 220.
pyautogui.click(200, 220)

# Move mouse 10 pixels down, that is, move the mouse relative to its current position.
pyautogui.move(None, 10)

# Double click the mouse at the current position
pyautogui.doubleClick()

# Use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

# Type with quarter-second pause in between each key.
pyautogui.write("Hello world!", interval=0.25)

# Simulate pressing the Escape key.
pyautogui.press("esc")

# hold down shift and press some stuff
pyautogui.keyDown("shift")
pyautogui.write(["left", "left", "left", "left", "left", "left"])
pyautogui.keyUp("shift")

# press ctrl-c
pyautogui.hotkey("ctrl", "c")
