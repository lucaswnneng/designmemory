import math

from mathHelper.geometry_helper import GeometryHelper
from mathHelper.point import Point
from mathHelper.segment import Segment


class ConcreteCrossSection:
    def __init__(
        self,
        vertexCoords: list[tuple[int, int]] | list[tuple[float, float]],
        rebarCoordMap,
        maxGridElementSize=1,
    ):
        if len(vertexCoords) < 3:
            raise AttributeError("Seção deve ter pelo menos 3 vértices")
        self.__getCoords(vertexCoords)
        self.__getExtremes()
        self.__normalizeCoords()
        self.__getSegments()
        self.__generateGrid(maxGridElementSize)
        self.__denormalizeCoords()
        self.__setRebarLocation(rebarCoordMap)

    def __getCoords(self, coords):
        self.coords = []
        for coord in coords:
            self.coords.append(Point(coord))

    def __getExtremes(self):
        self.nearX, self.nearY = self.coords[0].x, self.coords[0].y
        self.farX, self.farY = self.nearX, self.nearY

        for x, y in self.coords:
            if x < self.nearX:
                self.nearX = x
            if x > self.farX:
                self.farX = x
            if y < self.nearY:
                self.nearY = y
            if y > self.farY:
                self.farY = y

    def __normalizeCoords(self):
        newCoords = []
        for coord in self.coords:
            newCoords.append(Point((coord.x - self.nearX, coord.y - self.nearY)))
        self.coords = newCoords

    def __getSegments(self):
        self.segments = []
        pi = None
        pf = None
        for coordID in range(len(self.coords) - 1):
            pi = self.coords[coordID]
            pf = self.coords[coordID + 1]
            self.segments.append(Segment(pi, pf))
        self.segments.append(Segment(pf, self.coords[0]))

    def __generateGrid(self, maxGridElSize):
        xLen = self.farX - self.nearX
        self.xGridSize = math.ceil(xLen / maxGridElSize)
        self.xGridElSize = xLen / self.xGridSize

        yLen = self.farY - self.nearY
        self.yGridSize = math.ceil(yLen / maxGridElSize)
        self.yGridElSize = yLen / self.yGridSize

        self.gridElArea = self.xGridElSize * self.yGridElSize

        self.gridMap = []

        for xID in range(self.xGridSize):
            for yID in range(self.yGridSize):
                center = Point(
                    ((xID + 1 / 2) * self.xGridElSize, (yID + 1 / 2) * self.yGridElSize)
                )

                intersectionSeg = Segment(
                    center,
                    Point((center.x, center.y + self.yGridSize)),
                )

                nIntersections = 0
                for seg in self.segments:
                    if GeometryHelper.intersect(seg, intersectionSeg):
                        nIntersections += 1

                if nIntersections % 2 == 1:
                    self.gridMap.append((xID, yID))

    def __denormalizeCoords(self):
        newCoords = []
        for coord in self.coords:
            newCoords.append(Point((coord.x + self.nearX, coord.y + self.nearY)))
        self.coords = newCoords

    def __setRebarLocation(self, rebarCoordMap):
        self.rebarCoord = rebarCoordMap

    def getCenterElGridCoord(self, index):
        xID, yID = index
        return Point(
            (
                (xID + 1 / 2) * self.xGridElSize + self.nearX,
                (yID + 1 / 2) * self.yGridElSize + self.nearY,
            )
        )

    def getGridCoords(self):
        return [self.getCenterElGridCoord(p) for p in self.gridMap]
