from machine import Pin, ADC
import time

# Initialize the LED pin
led = Pin(18, Pin.OUT)

# Initialize the ADC (Analog to Digital Converter) pin for the light sensor
light_sensor = ADC(Pin(25)) # GPIO 25 is automatically set as input for ADC

# Define a threshold value to determine darkness
threshold = 2048  

while True:
    # Read the analog value from the light sensor
    light_value = light_sensor.read()
    
    # Print the light value for debugging (optional)
    print("Light Value:", light_value)
    
    # Check if the light value is below the threshold
    if light_value < threshold:
        led.value(1)  # Turn on the LED
    else:
        led.value(0)  # Turn off the LED
    
    # Delay for a short period
    time.sleep(1)
