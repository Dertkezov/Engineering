import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 100)
p.start(0)
try:
    while True:
        n = int(input())
        p.ChangeDutyCycle(n)
finally:
    p.stop()
    GPIO.cleanup()