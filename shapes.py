import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        A = math.pi *self.radius**2  
        return A 

    def circumference(self):
        C = 2*math.pi*self.radius  
        return C 

class Square:
    def __init__(self, side):  
        self.side = side

    def area(self):
        Area = self.side**2  
        return Area

    def perimeter(self):
        P = 4*self.side
        return P

class Rectangle:
    def __init__(self,w,l):
        self.l = l
        self.w = w
    def area(self):
        A = self.l * self.w
        return A

    def perimeter(self):
        P = 2 * (self.l + self.w)
        return P

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        A = 4 *(math.pi * self.radius**2)   
        return A 

    def volume(self):
        Volume = 4/3 *(math.pi * self.radius**3)
        return Volume
