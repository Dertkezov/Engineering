import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
import time
def tobin(N):
    return[int(i) for i in bin(N)[2:].zfill(8)]

try:
    while True:
        for i in range (0, 256):
            for j in range (len(dac)):
                GPIO.output(dac[j], int(tobin(i)[j])) 
                time.sleep(0.1)        
        for i in range (254, 0, -1):
            for j in range (len(dac)):
                GPIO.output(dac[j], int(tobin(i)[j]))
                time.sleep(0.1) 
        
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()