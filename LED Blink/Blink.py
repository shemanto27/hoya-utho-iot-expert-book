#step-1: impoting necessary modules
from machine import Pin
from time import sleep

#step-2: defining Pin and it's Mode
led = Pin(15, Pin.OUT)

#step-3: Running code continiously in loop 
while True:
  led.on()
  sleep(0.5)
  led.off()
  sleep(0.5)