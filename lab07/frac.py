def gcd(a,b):
    
    t = 0

    while b != 0:
        t = b
        b = a % b
        a = t
    
    return abs(a)


class Frac:

    def __init__(self, numer, denom):
        g = gcd(numer,denom)
        self._numer = numer // g
        self._denom = denom // g
    

    def add(self, frac):
        new_numer = self._numer * frac._denom + self._denom * frac._numer
        new_denom = self._denom * frac._denom  
        return Frac(new_numer,new_denom)


    def sub(self,frac):
        new_numer = self._numer * frac._denom - self._denom * frac._numer
        new_denom = self._denom * frac._denom
        if new_numer == 0:
            return 0
        else:  
            return Frac(new_numer,new_denom)

    def mul(self,frac):
        new_numer = self._numer * frac._numer
        new_denom = self._denom * frac._denom
        return Frac(new_numer, new_denom)

    def div(self,frac):
        new_numer = self._numer * frac._denom
        new_denom = self._denom * frac._numer
        return Frac(new_numer, new_denom)
    

    def __add__(self,frac):
        return self.add(frac)
    
    def __sub__(self,frac):
        return self.sub(frac)
    
    def __mul__(self,frac):
        return self.mul(frac)
    
    def __truediv__(self,frac):
        return self.div(frac)

    def __str__(self):
        return f'{self._numer}/{self._denom}'









x = Frac(1,6)
y = Frac(1,3)

z = x + y


print(z)




