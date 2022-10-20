
import numpy as np

#for a circle r^2 = x^2 + y^2, choose r = 1, so y = (1 - x^2)^1/2
#Acircle = pi * r^2
#pi = Acircle / (x^2 + y^2)
#use hit or miss to find Acircle
def f(x,r):
    return (r**2- x**2)**(1/2)
Ndarts = 100000
r = 1
a = 0
b = r
x = np.linspace(a,b,Ndarts)
y = f(x,r)
y_min = 0
y_max = np.max(y)
xrand = np.random.uniform(a,b, size = Ndarts)
yrand = np.random.uniform(y_min,y_max, size = Ndarts)
int_counter = np.sum(yrand < f(xrand,r))
Abox = (b-a)*(y_max-y_min)
Acircle = (int_counter / Ndarts)*Abox*4
print("using the hit or miss method with N =",Ndarts,", the area of a circle with radius",r,"is",Acircle)
#pi = Acircle/r^2 *4
pi = Acircle / (r**2)
print("from this circle, pi is calculated to be",pi)
print("")
#repeating with a different r value:
r = 2
a2 = 0
b2 = r
x2 = np.linspace(a2,b2,Ndarts)
y2 = f(x2,r)
y_min2 = 0
y_max2 = np.max(y2)
xrand2 = np.random.uniform(a2,b2, size = Ndarts)
yrand2 = np.random.uniform(y_min2,y_max2, size = Ndarts)
int_counter2 = np.sum(yrand2 < f(xrand2,r))
Abox2 = (b2-a2)*(y_max2-y_min2)
Acircle2 = (int_counter2 / Ndarts)* Abox2 *4
print("using the hit or miss method with N =",Ndarts,", the area of a circle with radius",r,"is",Acircle2)
#pi = Acircle/r^2 *4                                                                                                                                                       
pi2 = Acircle2 / (r**2)
print("from this circle, pi is calculated to be",pi2)


