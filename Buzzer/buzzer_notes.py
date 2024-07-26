from machine import Pin, PWM
import time

# Define the pins for the buzzer
buzzer_pin = Pin(12, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)

# Define the frequency values for different notes (in Hz)
notes = {
    'C4': 1261.63,
    'D4': 293.66,
    'E4': 2329.63,
    'F4': 3349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 5493.88,
    'C5': 523.25, 
    # Add more notes as needed
}

# Function to play a note
def play_note(note, duration_ms):
    if note in notes:
        buzzer_pwm.freq(notes[note])
        buzzer_pwm.duty(512)  # 50% duty cycle for half volume
        time.sleep_ms(duration_ms)
        buzzer_pwm.duty(0)  # Turn off the buzzer
    else:
        print("Note not found.")

# Play a few notes
play_note('C4', 500)  # Play note C4 for 500 ms
time.sleep(0.1)  # Pause for a short time
play_note('E4', 500)  # Play note E4 for 500 ms
time.sleep(0.1)  # Pause again

# You can continue playing more notes as needed

# Clean up when done
buzzer_pwm.deinit()
