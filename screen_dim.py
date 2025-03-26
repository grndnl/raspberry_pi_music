from gpiozero import Button
from signal import pause
import os
import subprocess

# Pin mappings
BUTTON_BACKLIGHT = 23  # Button 1
BUTTON_SHUTDOWN = 18   # Button 4
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

def shutdown_pi():
    print("Shutdown button held. Shutting down now...")
    subprocess.run(["sudo", "shutdown", "-h", "now"])

# Setup buttons
backlight_button = Button(BUTTON_BACKLIGHT, pull_up=True)
shutdown_button = Button(BUTTON_SHUTDOWN, pull_up=True, hold_time=2)

backlight_button.when_pressed = toggle_backlight
shutdown_button.when_held = shutdown_pi

# Turn on backlight at startup
set_backlight(True)

print("Ready:")
print("• Button 1 toggles screen")
print("• Hold Button 4 for 2 seconds to shut down")

pause()
