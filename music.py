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

# Read button state
# Button state is True when pressed (i.e. inverts raw state of button)
state = True

while True:
    if pitft.Button1:
        print("pressed button 1")
        pitft.Backlight(state)
        state = not state