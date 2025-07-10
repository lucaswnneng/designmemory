from .vector import *
from .point import *
import numpy as np


class CoordinatesBase2D:
    def __init__(self, origin: Point, v1: Vector, v2: Vector):
        self.origin = origin
        self.v1 = v1
        self.v2 = v2
        self.__getTransformationMatrix()

    def __getTransformationMatrix(self):
        m = np.column_stack(
            [[self.v1.point.x, self.v1.point.y], [self.v2.point.x, self.v2.point.y]]
        )
        self.transformMatrix = np.linalg.inv(m)
    
    def getTransformCoordinates(self, point: Point):
        desloc = point - self.origin
        vg = np.array([desloc.x, desloc.y])
        vl = self.transformMatrix @ vg
        return Point((vl[0], vl[1]))
