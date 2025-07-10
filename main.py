import matplotlib.pyplot as plt
from section.concrete_cross_section import ConcreteCrossSection
from mathHelper.point import Point
from mathHelper.geometry_helper import GeometryHelper
from section.concrete_oblique_bending import ConcreteObliqueBending
from section.concrete import Concrete


def main():
    coords = [(-5, -10), (10, -5), (5, 10), (-10, 5)]
    rebarCoords = {(-2.5, -5): 12.5, (5, -2.5): 20, (-5, 2.5): 16, (2.5, 5): 10}
    gridElementSize = 0.5

    sec = ConcreteCrossSection(
        coords,
        rebarCoords,
        gridElementSize,
    )

    fco = ConcreteObliqueBending(sec, Concrete(30,1.4))
    ln = GeometryHelper.lineEquation(Point((0,0)), Point((0,1)))
    points = fco.filterCompressedElements(ln, isAbove=False)

    x, y = zip(*points)
    xBar, yBar = zip(*[(xi, yi) for xi, yi in sec.rebarCoord.keys()])
    plt.scatter(x, y)
    plt.scatter(xBar, yBar)
    print(sec.coords)
    plt.show()


if __name__ == "__main__":
    main()
