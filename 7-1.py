#Импорт необходимых библиотек для работы с GPIO b=и построения графиков
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time
#Объявление пинов
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

#Создание функции, переводящей число в массив в двоичном представлении
def tobin(N):
    return[int(i) for i in bin(N)[2:].zfill(8)]

#Функция, которая определяет значение напряжения
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

#Создаем список чисел, которые пропорциональны напряжению
list = []
try:
    GPIO.output(troyka, 1)
    k = 0
    start = time.time()
    s = 0
    p = -1
    k = 0
    while k < 100:
        k += 1
        list.append(adc())
        if p < adc():
            p = adc()
            if s == 0:
                print('Заряжается')
                s += 1
        elif (p == adc() and s == 1):
            print('Заряжен')
            s += 1
        elif p > adc():
            p = adc()
            if s == 2:
                print('Разрядка')
                s = 0
    finish = time.time()
except KeyboardInterrupt:
    pass

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

#Определение времени эксперимента и частоты дескритизации
t = finish - start
v = t / k
print(t)
print(v)
t = str(t)
v = str(v)

#Построение графика
plt.plot(list)
plt.show()

#Запись полученных значений в файлы
lists = [str(i) for i in list]
with open ('data.txt', 'w') as outf:
    outf.write("\n".join(lists))
with open ('settings2.txt', 'w') as outf:
    outf.write(f"Время эксперимента: {t}\n")
    outf.write(f"Частота дескритизации: {v}\n")
with open ('settings.txt', 'w') as outf:
    outf.write(f"{t}\n")
    outf.write(f"{v}\n")