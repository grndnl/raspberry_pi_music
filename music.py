from pitftscreen import PiTFT_Screen
import webbrowser
import time

# start browswer
# URL you want to open
url = "https://music.youtube.com/"

# Optional delay to ensure desktop has loaded (seconds)
time.sleep(5)

# Open URL in the default browser
print("Opening URL")
webbrowser.open(url)

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