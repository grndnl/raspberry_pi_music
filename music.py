from pitftscreen import PiTFT_Screen
import webbrowser
import time
import os

# start browswer
# URL you want to open
url = "https://music.youtube.com/"

# Optional delay to ensure desktop has loaded (seconds)
time.sleep(5)

# Open URL in the default browser
print("Opening URL")
# os.system(f"chromium-browser --kiosk {url}")
chromium_path = '/usr/bin/chromium-browser %s'
webbrowser.get(chromium_path).open(url)


# Screen loop
pitft = PiTFT_Screen()

# Set a callback
# pitft.Button1Interrupt(name_of_callback_method)

# Turn off back light
# pitft.Backlight(False)

# Turn it back on
# pitft.Backlight(True)



def toggle_backlight(channel):
    """Callback function to toggle the backlight."""
    pitft.Backlight(not pitft.backlightenabled)

# Set a callback for Button 1 to toggle the backlight
pitft.Button1Interrupt(callback=toggle_backlight)

while True:
    print('waiting..')
    time.sleep(1)