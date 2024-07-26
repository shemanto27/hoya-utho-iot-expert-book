# Step 1: Importing necessary modules
from machine import SoftI2C, Pin
from utime import sleep
from i2c_lcd import I2cLcd 

# I2C address of the LCD
AddressOfLcd = 0x27

# Initialize I2C for the LCD
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000) # connect scl to GPIO 22, sda to GPIO 21

# Initialize the LCD
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)

# Step 2: Display message on the LCD
lcd.move_to(0, 0)
lcd.putstr("Hello IoT")
lcd.move_to(0, 1)
lcd.putstr("Learner")

# Keep the message displayed
while True:
    sleep(1)
