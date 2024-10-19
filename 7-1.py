import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
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

def adc():
    V = 0
    for i in range (8):
        S = 2 ** (7 - i)
        GPIO.output(dac, tobin(V + S))
        time.sleep(0.01)
        CV = GPIO.input(comp)
        if CV == 0:
            V += S
    return(V)

list = []
try:
    GPIO.output(troyka, 1)
    k = 0
    start = time.time()
    while k < 100:
        list.append(adc())
        k += 1
    finish = time.time()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

t = finish - start
print(str(t))
print(t / 100)
print(100 / t)
plt.plot(list)
plt.show()

lists = [str(i) for i in list]
with open ('data.txt', 'w') as outf:
    outf.write("\n".join(lists))
with open ('settings.txt', 'w') as outf:
    outf.write("Время: ", str(t))
    # outf.write("\n".join(str(t / 100)))
    # outf.write("\n".join(str(100 / t)))