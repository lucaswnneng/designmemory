from .concrete_cross_section import ConcreteCrossSection
from .concrete import Concrete
from mathHelper.segment import Segment
from mathHelper.geometry_helper import GeometryHelper
from mathHelper.point import Point


class ConcreteObliqueBending:
    def __init__(self, section: ConcreteCrossSection, concrete: Concrete):
        self.section = section
        self.concrete = concrete

    def getConcreteForceAtElement(self, index, ec):
        x, y = self.section.getCenterElGridCoord(index)
        stress = self.concrete.getStress(ec)
        return self.section.gridElArea * stress

    def getNeutralLineHeight(ei, ef, h):
        """
        reference point: top of h
        positive result: neutral line under top of h
        positive deformation: compression
        """
        return -ei * h / (ef - ei)

    def filterCompressedElements(self, neutralLineEquation: tuple[float, float], isAbove):
        a, b = neutralLineEquation
        minX = self.section.nearX
        maxX = self.section.farX
        minY = a * minX + b
        maxY = a * maxX + b
        neutralLineSegment = Segment(Point((minX, minY)), Point((maxX, maxY)))
        return GeometryHelper.filterPointsBySegment(
            self.section.getGridCoords(), neutralLineSegment, isAbove
        )
