#step-1: impoting necessary modules
from machine import Pin, I2C
import ssd1306

#step-2: telling ESP32 where our sensor's data pin is connected
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#step-3: reading data continuously inside loop
while True:
  try:
    oled.text('Hello World!', 10, 10)      
    oled.show()

  except OSError as e: # Error Handling  
    print("Error Data")
