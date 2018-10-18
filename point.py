from math import sqrt

class Point:
    def __init__ ( self , x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __str__ (self):
        return ("{},{}").format(self.x, self.y)

    def distance_from_origin(self):
        d = sqrt (self.x ** 2 + self.y ** 2)
        return d

    def __add__ (self,p):
        add = (self.x + self.y)
        return add



print ("p.x {}, p.y = {}".format(p.x, p.y))
    p = Point(x = 3, y = 4)
