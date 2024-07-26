# code written by Shemanto Sharkar (let's connect on LinkedIn: https://www.linkedin.com/in/shemanto/)
#step-1: impoting necessary modules
from machine import Pin
from utime import sleep
import dht
from machine import SoftI2C, Pin
from i2c_lcd import I2cLcd 

AddressOfLcd = 0x27
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000) # connect scl to GPIO 22, sda to GPIO 21
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)

#step-2: telling ESP32 where our sensor's data pin is connected
sensor = dht.DHT22(Pin(13))

Thermometer_icon = bytearray([0x04,0x0A,0x0A,0x0E,0x1F,0x1F,0x0E,0x0E])
Waterdrop_icon = bytearray([0x04,0x04,0x0A,0x0A,0x11,0x11,0x11,0x0E])
wind_icon = bytearray([0x00,0x1C,0x10,0x1F,0x03,0x1F,0x10,0x1C])

lcd.custom_char(0, Thermometer_icon)
lcd.custom_char(1, Waterdrop_icon)

#step-3: reading data continuously inside loop
while True:
  try:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    lcd.move_to(0,0)
    lcd.putstr(chr(0) + "T=" + str(t) + "C" + chr(1) + "H=" + str(h) + "%")
    #lcd.move_to(0,1)
    sleep(2)
    
  except OSError as e: # Error Handling  
    lcd.move_to(0,0)
    lcd.putstr("Error Data")
