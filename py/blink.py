import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

def on():
    GPIO.output(13, True)
    time.sleep(0.5)
    GPIO.output(13, False)
    time.sleep(0.5)
    return

def off():
    GPIO.cleanup()
    return

try:
    f = open('../_model/blink.txt', 'r+')
    while True:
        time.sleep(1)
        f.seek(0)
        resp = f.read()
        if (resp == "on"):
            on()
except KeyboardInterrupt:
    off()