import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Setup
reader = SimpleMFRC522()

try:
    print("Mohon arahkan kartu RFID ke reader")
    id, text = reader.read()
    print(f"ID: {id}")
    print(f"Teks: {text}")
finally:
    GPIO.cleanup()
  
