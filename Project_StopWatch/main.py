from machine import Pin, I2C
import ssd1306
import time

# Initialize OLED display
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Initialize buttons
start_button = Pin(2, Pin.IN, Pin.PULL_UP)
stop_button = Pin(4, Pin.IN, Pin.PULL_UP)
reset_button = Pin(5, Pin.IN, Pin.PULL_UP)

# Initialize variables for stopwatch
start_time = 0
total_time = 0
active = False
lin_hight = 5
col_width = 8
led = Pin(25, Pin.OUT)

def text_write(text, lin, col=0):
    oled.text(text, col*col_width, lin*lin_hight)
 
def time_text(time_ms):
    millis = time_ms % 1000
    seconds = (time_ms // 1000) % 60
    minutes = (time_ms // 60000) % 60
    hours = (time_ms // 3600000) % 24
    return "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, millis)

def show():
    oled.fill(0)
    total_text = time_text(total_time)
    text_write(total_text, 6, 2)
    oled.show()

# Main loop
while True:
    if not active:
        led.value(0) 
        if not start_button.value():  # Start button pressed
            start_time = time.ticks_ms() - total_time  # Continue from where it stopped
            active = True
            while not start_button.value():  # Debounce
                time.sleep(0.01)
                
    if active:
        led.value(1)
        total_time = time.ticks_ms() - start_time
        if not stop_button.value():  # Stop button pressed
            active = False
            while not stop_button.value():  # Debounce
                time.sleep(0.01)
    
    if not active and not reset_button.value():  # Reset button pressed
        total_time = 0
        show()  # Update the display immediately
        while not reset_button.value():  # Debounce
            time.sleep(0.01)
    
    show()
    time.sleep(0.1)
