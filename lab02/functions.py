def to_km(mile):
    km = 1609.344 * mile
    return km/1000

def to_fahrenheit(c):
    f = (9/5) * c + 32
    return f

def to_celsius(f):
    c = (5/9)*(f - 32)
    return c

def print_c2f_table(start, stop):
    for num in range(start, stop):
        print(num, to_fahrenheit(num))
        


print_c2f_table(3,5)