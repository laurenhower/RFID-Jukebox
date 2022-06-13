import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('Type Spotify UDI:')
    print('Scan RFID card:')
    reader.write(text)
    print('Write Successful :D')
finally:
    GPIO.cleanup()
    