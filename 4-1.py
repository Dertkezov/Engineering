import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def tobin(N):
    return[int(i) for i in bin(N)[2:].zfill(8)]
try:
    while True:
        N = int(input())
        for i in range (len(dac)):
            GPIO.output(dac[i], (tobin(N)[i]))
        print(3.3/256*N)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()