import matplotlib.pyplot as plt
from section.concrete_cross_section import ConcreteCrossSection
from mathHelper.point import Point
from mathHelper.segment import Segment
from mathHelper.geometry_helper import GeometryHelper
from section.concrete_oblique_bending import ConcreteObliqueBending
from section.concrete import Concrete
from section.deformation import Deformation
import math


def main():
    coords = [(-5, -10), (10, -5), (5, 10), (-10, 5)]
    voidCoordsList = [[(-1, -1), (1, -1), (1, 1), (-1, 1)], [(2, 2), (5, 2), (3, 6)]]
    rebarCoords = {(-2.5, -5): 12.5, (5, -2.5): 20, (-5, 2.5): 16, (2.5, 5): 10}
    gridElementSize = .5

    sec = ConcreteCrossSection(
        coords,
        rebarCoords,
        voidCoordsList,
        gridElementSize,
    )

    fco = ConcreteObliqueBending(sec, Concrete(30, 1.4))
    plane = ConcreteObliqueBending.getDeformationPlaneFunction(
        Deformation(Point((-5, -5)), 0),
        Deformation(Point((5, 5)), 0),
        Deformation(Point((-5, 5)), 0.001),
    )
    forces = fco.getConcreteForcesAtElements(plane)
    points = forces.keys()
    values = forces.values()

    if points:
        x, y = zip(*points)
        plt.scatter(x, y, c=values, cmap="viridis")
        plt.colorbar(label="valores associados")

    if sec.rebarCoord:
        xBar, yBar = zip(*[(xi, yi) for xi, yi in sec.rebarCoord.keys()])
        plt.scatter(xBar, yBar)

    secX, secY = zip(*coords)
    plt.plot(secX, secY)

    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")
    plt.show()


if __name__ == "__main__":
    main()
