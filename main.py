import matplotlib.pyplot as plt
from section.concrete_cross_section import ConcreteCrossSection
from mathHelper.point import Point
from mathHelper.segment import Segment
from mathHelper.geometry_helper import GeometryHelper
from section.concrete_oblique_bending import ConcreteObliqueBending
from section.concrete import Concrete
import math


def main():
    coords = [(-5, -10), (10, -5), (5, 10), (-10, 5)]
    re = 10
    ri = 5
    coords = [(math.cos(math.radians(a)) * re, math.sin(math.radians(a)) * re) for a in range(0,360,10)]
    voidCoordsList = [[(-1, -1), (1, -1), (1, 1), (-1, 1)], [(2,2),(5,2),(3,6)]]
    voidCoordsList = [[(math.cos(math.radians(a)) * ri, math.sin(math.radians(a)) * ri) for a in range(0,360,10)]]
    rebarCoords = {(-2.5, -5): 12.5, (5, -2.5): 20, (-5, 2.5): 16, (2.5, 5): 10}
    gridElementSize = 0.2

    sec = ConcreteCrossSection(
        coords,
        [],
        voidCoordsList,
        gridElementSize,
    )

    fco = ConcreteObliqueBending(sec, Concrete(30, 1.4))
    ln = Segment(Point((0, 0)), Point((1, 0)))
    #points = fco.filterCompressedElements(ln, isAbove=True)
    points = fco.section.getGridCoords()

    if points:
        x, y = zip(*points)
        plt.scatter(x, y)

    if sec.rebarCoord:
        xBar, yBar = zip(*[(xi, yi) for xi, yi in sec.rebarCoord.keys()])
        plt.scatter(xBar, yBar)
    
    secX, secY = zip(*coords)
    plt.plot(secX, secY)
    voidX, voidY = zip(*voidCoordsList[0])
    plt.plot(voidX, voidY)

    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")
    plt.show()


if __name__ == "__main__":
    main()
