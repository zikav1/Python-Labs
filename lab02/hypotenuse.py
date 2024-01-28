import math


def hypotenuse(a,b):
    c = math.sqrt(a**2+b**2)
    return c


def distance(x1,x2,y1,y2):
    difx = x2 - x1
    dify = y2 - y1
    return hypotenuse(difx, dify)

x1 = float(input("Ange en sida x1 "))
x2 = float(input("Ange en sida x2 "))
y1 = float(input("Ange en till sida y1 "))
y2 = float(input("Ange en till sida y2 "))

print("Hypotenusan är", distance(x1,x2,y1,y2))

