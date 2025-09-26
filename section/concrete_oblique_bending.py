from .concrete_cross_section import ConcreteCrossSection
from .deformation import Deformation
from .concrete import Concrete
from mathHelper.segment import Segment
from mathHelper.geometry_helper import GeometryHelper
from mathHelper.point import Point


class ConcreteObliqueBending:
    def __init__(self, section: ConcreteCrossSection, concrete: Concrete):
        self.section = section
        self.concrete = concrete

    def getConcreteForceAtElement(self, ec):
        return self.section.gridElArea * self.concrete.getStress(ec)

    def getDeformationPlaneFunction(d1, d2, d3):
        v1 = Deformation(
            Point((d2.coord.x - d1.coord.x, d2.coord.y - d1.coord.y)), d2.e - d1.e
        )

        v2 = Deformation(
            Point((d3.coord.x - d1.coord.x, d3.coord.y - d1.coord.y)), d3.e - d1.e
        )

        normal_d = Deformation(
            Point(
                (
                    v1.coord.y * v2.e - v1.e * v2.coord.y,
                    v1.e * v2.coord.x - v1.coord.x * v2.e,
                )
            ),
            v1.coord.x * v2.coord.y - v1.coord.y * v2.coord.x,
        )

        d = -(
            normal_d.coord.x * d3.coord.x
            + normal_d.coord.y * d3.coord.y
            + normal_d.e * d3.e
        )

        return (
            lambda x, y: -(normal_d.coord.x * x + normal_d.coord.y * y + d) / normal_d.e
        )

    def getConcreteForcesAtElements(self, planeFunction):
        ret = dict()
        for coord in self.section.getGridCoords():
            e = planeFunction(coord.x, coord.y)
            ret[coord] = self.getConcreteForceAtElement(e)

        return ret

    def getNeutralLineHeight(ei, ef, h):
        """
        reference point: top of h
        positive result: neutral line under top of h
        positive deformation: compression
        """
        return -ei * h / (ef - ei)

    def filterCompressedElements(self, neutralLineSegment: Segment, isAbove):
        return GeometryHelper.filterPointsBySegment(
            self.section.getGridCoords(), neutralLineSegment, isAbove
        )

    def getNeutralLineSegment(angle, height):
        pass
