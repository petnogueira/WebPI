import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

try:
    f = open('workfile', 'r+')
    while true:
        f.seek(0)
        resp = f.read()
        if (resp = "on"):
            on()
        else:
            off()
except KeyboardInterrupt:
    off()

def on():
    GPIO.output(13, True)
    time.sleep(0.5)
    GPIO.output(13, False)
    time.sleep(0.5)

def off():
    GPIO.cleanup()