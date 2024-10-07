import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

def tobin(N):
    return[int(i) for i in bin(N)[2:].zfill(8)]

def sum(a):
    s = 0
    for i in range (7, -1, -1):
        s += a[i] * 2 ** i
    return(s)

def adc():
    V = 0
    for i in range (8):
        S = 2 ** (7 - i)
        GPIO.output(dac, tobin(V + S))
        time.sleep(0.01)
        CV = GPIO.input(comp)
        if CV == 0:
            V += S
    return(V * 3.3 / 256)

try:
    while True:
        print(adc())
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
