from .segment import *
from .vector import *


class GeometryHelper:
    def intersect(seg1: Segment, seg2: Segment):
        d1 = GeometryHelper.direction(seg2.p1, seg2.p2, seg1.p1)
        d2 = GeometryHelper.direction(seg2.p1, seg2.p2, seg1.p2)
        d3 = GeometryHelper.direction(seg1.p1, seg1.p2, seg2.p1)
        d4 = GeometryHelper.direction(seg1.p1, seg1.p2, seg2.p2)

        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and (
            (d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)
        ):
            return True

        return False

    def direction(p0: Point, p1: Point, p2: Point):
        return (p1.x - p0.x) * (p2.y - p0.y) - (p2.x - p0.x) * (p1.y - p0.y)

    def getHighestPointOnList(points: list[Point]):
        return max(points, key=lambda p: p.y)

    def filterPointsBySegment(points: list[Point], segment: Segment, isAbove: bool):
        scaleFactor = segment.squaredLength() + 2
        segVector = GeometryHelper.vectorizeSegment(segment)
        perpendicularVector = (
            Vector(Point((-segVector.point.y, segVector.point.x)))
            if isAbove
            else Vector(Point((segVector.point.y, -segVector.point.x)))
        ) * scaleFactor * 100
        

        filter = []
        maxY = GeometryHelper.getHighestPointOnList(points).y + 1
        for point in points:
            intersectionSeg = GeometryHelper.segmentByVector(perpendicularVector, point)

            if not GeometryHelper.intersect(segment, intersectionSeg):
                filter.append(point)

        return filter

    def vectorizeSegment(segment: Segment):
        return Vector(segment.p2 - segment.p1)

    def segmentByVector(vector: Vector, origin: Point):
        return Segment(origin, vector.point + origin)

    def lineEquation(p1: Point, p2: Point):
        """
        return a and b coefficients
        """
        xi, yi = p1
        xf, yf = p2
        a = (yf - yi) / (xf - xi)
        b = -a * xi + yi
        return (a, b)
