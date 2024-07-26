#step-1: impoting necessary modules
from hcsr04 import HCSR04
from time import sleep

#step-2: telling ESP32 where our sensor's pins are connected
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)


#step-3: reading data continuously inside loop
while True:
  try:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)

  except OSError as e: # Error Handling  
    print("Error Data")