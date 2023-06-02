import time
import random
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyboardController, Key, Listener
import pyautogui

# Initialize mouse and keyboard controller
mouse = Controller()
keyboard = KeyboardController()

# Get screen size
screen_width, screen_height = pyautogui.size()

# Initialize the running flag
running = True

def on_press(key):
    global running
    # Stop listener when ESC is pressed
    if key == Key.esc:
        running = False

# Start the listener
listener = Listener(on_press=on_press)
listener.start()

def switch_tab():
    # Switch to the next tab
    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

def scroll_tab(direction):
    # Scroll up or down
    if direction == "up":
        mouse.scroll(0, 2)
    elif direction == "down":
        mouse.scroll(0, -2)

while running:
    # Randomly move mouse
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    mouse.position = (x, y)
    time.sleep(random.uniform(0.5, 1.5))  # wait for a random interval

    # Randomly switch between tabs
    if random.random() < 0.3:  # 30% chance to switch tab
        switch_tab()
        time.sleep(random.uniform(0.5, 1.5))  # wait for a random interval

    # Randomly scroll up or down
    if random.random() < 0.3:  # 30% chance to scroll
        scroll_direction = "up" if random.random() < 0.5 else "down"
        scroll_tab(scroll_direction)
        time.sleep(random.uniform(0.5, 1.5))  # wait for a random interval

# Stop the listener when the script is done
listener.stop()
print('Goodbye!')