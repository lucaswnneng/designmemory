from .point import Point
import math

class Vector:
    def __init__(self, point: Point):
        self.point = point
    
    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return Vector(Point((self.point.x * other, self.point.y * other)))
        elif isinstance(other, Vector):
            return Vector(Point((self.point.x * other.point.x, self.point.y * other.point.y)))
        
        return ValueError('Objeto deve ser vetor ou escalar')
    
    def __rmul__(self, other):
        if isinstance(other, (int,float)):
            return Vector(Point((self.point.x * other, self.point.y * other)))
        elif isinstance(other, Vector):
            return Vector(Point((self.point.x * other.point.x, self.point.y * other.point.y)))
        
        return ValueError('Objeto deve ser vetor ou escalar')
    
    @property
    def length(self):
        return math.sqrt(self.point.x ** 2 + self.point.y ** 2)
    
    def normalize(self):
        v = Vector(self.point) * (1/self.length)
        self.point.x = v.point.x
        self.point.y = v.point.y
    
    def counterClockwisePerp(self):
        return Vector(-self.point.y, self.point.x)