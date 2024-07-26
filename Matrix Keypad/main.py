from machine import Pin
from keypad import Keypad
from time import sleep

# Define GPIO pins for rows
row_pins = [Pin(15),Pin(2),Pin(4),Pin(5)]

# Define GPIO pins for columns
column_pins = [Pin(18),Pin(19),Pin(21),Pin(22)]

# Define keypad layout
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']]

keypad = Keypad(row_pins, column_pins, keys)

while True:
    key_pressed = keypad.read_keypad()
    if key_pressed:
        print("Key pressed:", key_pressed)
    sleep(0.1)  # debounce and delay