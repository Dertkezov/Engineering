import matplotlib.pyplot as plt
data = open("data.txt")
settings = open("settings.txt")
a = [(int(x) / 256 * 3.3) for x in data]
t = settings.readline()
v = settings.readline()
t = float(t)
v = float(v)
time = []
m = m1 = 0
for i in range (0, len(a)):
    time.append(i * v)
for i in range (2, len(a) - 1):
    if a[i + 1] == a[i]:
        m = time[i]
    if a[i - 2] > a[i - 1] and a[i] > a[i - 1]:
        m1 = time[i]
        break
fig, ax = plt.subplots(figsize = (8, 8), dpi = 200)
ax.set_ylim(0, 3.3)
ax.set_xlim(0, 30)
plt.plot(time[::2], a[::2], '-o', c = "green", linewidth = 2)
plt.legend(['V(t)'])
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.title('Процесс заряда и разряда конденсатора в RC - цепочке')
plt.grid(which = 'major', linewidth = 1.6)
plt.grid(which = 'minor', linewidth = 0.4)
plt.minorticks_on()
plt.text(0.2, 2.8, f'Время заряда: {m} с', fontsize = 6)
plt.text(0.2, 3.0, f'Время разряда: {round(m1 - m,2)} с', fontsize = 6)
plt.savefig('Graph.svg')
plt.show()