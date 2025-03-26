from gpiozero import Button
from signal import pause
import os

BUTTON_PIN = 23
BACKLIGHT_PATH = "/sys/class/backlight/soc:backlight/brightness"

# Track backlight state
backlight_on = True

def set_backlight(state):
    try:
        with open(BACKLIGHT_PATH, "w") as f:
            f.write("1" if state else "0")
        print(f"Backlight {'ON' if state else 'OFF'}")
    except Exception as e:
        print("Failed to toggle backlight:", e)

def toggle_backlight():
    global backlight_on
    backlight_on = not backlight_on
    set_backlight(backlight_on)

# Set up the button (BCM pin 23)
button = Button(BUTTON_PIN, pull_up=True)
button.when_pressed = toggle_backlight

# Turn on backlight at startup
set_backlight(True)

print("Press Button 1 (GPIO 23) to toggle the backlight.")
pause()
