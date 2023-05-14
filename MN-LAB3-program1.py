import matplotlib.pyplot as plt
import numpy as np

n = int(input("Podaj wartosc n: "))
h = float(input("Podaj wartosc skoku h: "))

y = np.zeros(n)

x0 = float(input("Podaj wartosc x0: "))
y[0] = float(input("Podaj wartosc y0: "))

a = float(input("Podaj wartosc a: "))
b = float(input("Podaj wartosc b: "))

print("Wybierz postac funkcji F(x, y):")
print("1. F(x, y) = a*x + b*y")
print("2. F(x, y) = a*x - b*y")
print("3. F(x, y) = a*x * b*y")
print("4. F(x, y) = a*x / b*y")
wybor = int(input("Twoj wybor: "))


def funkcja(a, b, x, y, wybor):
    if wybor == 1:
        return (a * x) + (b * y)
    elif wybor == 2:
        return (a * x) - (b * y)
    elif wybor == 3:
        return (a * x) * (b * y)
    elif wybor == 4:
        return (a * x) / (b * y)


x_wartosci = np.zeros(n-1)
for i in range(n-1):
    x_wartosci[i] = x0 + i * h
    y[i+1] = y[i] + h * funkcja(a, b, x_wartosci[i], y[i], wybor)


x_wartosci2 = np.zeros(n)
for i in range(n):
    x_wartosci2[i] = x0 + i * h;
    print(f"x = {x_wartosci2[i]}, y = {y[i]}")

plt.plot(x_wartosci2, y, 'ks', markerfacecolor='none')
plt.plot(x_wartosci2, y, 'r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("MN-LAB3: Metoda Eulera")
plt.grid(True)
plt.show()

