import time
from pitftscreen import PiTFT_Screen

# Initialize screen
pitft = PiTFT_Screen()

# Define callback to toggle backlight
def toggle_backlight(channel):
    pitft.Backlight(not pitft.backlightenabled)

# Set up interrupt on Button 1
pitft.Button1Interrupt(callback=toggle_backlight)

# Keep script running
while True:
    print('waiting..')
    time.sleep(1)
