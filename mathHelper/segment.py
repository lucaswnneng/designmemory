from .point import *

class Segment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"({self.p1}, {self.p2})"
    
    def squaredLength(self):
        return (self.p2.x-self.p1.x) ** 2 + (self.p2.y-self.p1.y) ** 2