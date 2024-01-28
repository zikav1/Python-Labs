import math


print("Ange två tal:")
x = float(input())
y = float(input())

print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "*", y, "=", x * y)
print(x, "/", y, "=", x / y)



def hypotenuse(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

print('Längden på sträckan är', hypotenuse(10,5))