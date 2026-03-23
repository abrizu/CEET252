import math
class Area:
    def __init__(self, p1, p2 = 0.0):   # default for p2 = 0.0 if not assigned
        self.p1 = p1
        self.p2 = p2

    def square(self):
        return self.p1 ** 2

    def rectangle(self):
        return self.p1 * self.p2 
    
    def circle(self):
        return round(math.pi * self.p1 ** 2, 6)

S1 = Area(1.0, 2.0)    # pass the attributes, p2 is for rectangle only
print(format(S1.square(), '.3f'))
print(format(S1.rectangle(), '.3f'))
print(format(S1.circle(), '.3f'))