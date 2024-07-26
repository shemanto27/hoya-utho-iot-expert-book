import time
from machine import Pin

# Initialize LEDs
LED1 = Pin(14, Pin.OUT) # Red LED
LED2 = Pin(12, Pin.OUT) # Yellow LED
LED3 = Pin(13, Pin.OUT) # Green LED

# Traffic light sequence
while True:
    # Red light ON, Yellow and Green lights OFF
    LED1.value(1) # Red LED on
    LED2.value(0) # Yellow LED off
    LED3.value(0) # Green LED off
    time.sleep(8) # 8 seconds of red light (STOP!)

    # Yellow light ON, Red and Green lights OFF
    LED1.value(0) # Red LED off
    LED2.value(1) # Yellow LED on
    LED3.value(0) # Green LED off
    time.sleep(2) # 2 seconds of yellow light (GET READY)

    # Green light ON, Red and Yellow lights OFF
    LED1.value(0) # Red LED off
    LED2.value(0) # Yellow LED off
    LED3.value(1) # Green LED on
    time.sleep(5) # 5 seconds of green light (GO!)

    # Yellow light ON, Red and Green lights OFF
    LED1.value(0) # Red LED off
    LED2.value(1) # Yellow LED on
    LED3.value(0) # Green LED off
    time.sleep(2) # 2 seconds of yellow light (GET READY)
