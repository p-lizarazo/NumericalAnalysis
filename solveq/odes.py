import matplotlib.pyplot as plt
import math
"""
Considere el PVI: y' = y+x ; y(0)=1
Resultado analitico, sol particular: y(x)= -x+2*e^(x)-1
"""
def oderesult(x):
    return (-x+2 * math.exp(x) -1)

"""
Esto es f(t,y(t)), para algun t
"""
def dfunction(x,y):
    return (y+x)

"""
Metodo Euler es: y(t+h) es aproximado por y(t)+hy'(t) = y(t) + h*f(t,y(t))
"""
def Euler(f, xa, xb, ya, n):
    _xs = []
    _ys = []
    h = (xb-xa)/n
    _ys.append(xa)
    _xs.append(ya)
    x = xa
    y = ya
    while x <= xb:
        y += h * f(x, y)
        x += h
        _ys.append(y)
        _xs.append(x)
    return _xs, _ys

"""
"""
def modifiedEuler(f,xa,xb,ya,n):
    _xs = []
    _ys = []
    h = (xb-xa)/n
    _ys.append(xa)
    _xs.append(ya)
    x = xa
    y = ya
    while x <= xb:
        y = y + h*f(x+1/2*h,y+1/2*h*f(x,y))
        x = x + h
        _ys.append(y)
        _xs.append(x)
    return _xs, _ys

n = int(input("En cuantos pedazos quiere partir el intervalo: "))
x_b = float(input("Inserte un num mayor a 0, hasta donde quiera graficar: "))

x_s= []
y_s = []
h = 0.05
for i in range(int(x_b/h)):
    y_s.append(oderesult(i*h))
    x_s.append(i*h)

x1_s, y1_s = Euler(dfunction, 0, x_b, 1, n)
x2_s, y2_s = modifiedEuler(dfunction, 0,x_b,1,n)
plt.plot(x_s, y_s)
plt.plot(x1_s,y1_s)
plt.plot(x2_s,y2_s)
plt.show()
