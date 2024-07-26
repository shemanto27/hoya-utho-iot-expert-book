from machine import Pin, I2C
import ssd1306
import time

# Initialize OLED display
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Function to format time into HH:MM:SS
def time_text(elapsed_time):
    secs = elapsed_time % 60
    mins = (elapsed_time // 60) % 60
    hours = (elapsed_time // 3600) % 24
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)

# Function to display time on OLED
def show():
    oled.fill(0)
    elapsed_time = int(time.time())
    total_text = time_text(elapsed_time)
    oled.text(total_text, 0, 28)  # Center the text horizontally
    oled.show()

# Main loop to update the display every second
while True:
    show()
    time.sleep(1)
