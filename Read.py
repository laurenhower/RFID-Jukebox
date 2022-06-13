#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        print("Waiting for you to scan an RFID sticker/card")
        id, text = reader.read()
        print("The texr for this card is:", text.strip())
        
finally:
        GPIO.cleanup()