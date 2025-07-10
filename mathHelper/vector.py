from .point import Point

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