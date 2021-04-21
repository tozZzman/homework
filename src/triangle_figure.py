import math
from .base_figure import Figure


class Triangle(Figure):
    def __init__(self, name, sides):
        super().__init__(name, sides, angles=3)
        if len(sides) != 3:
            raise Exception('У треугольника должно быть три стороны!')
        else:
            self.sides = sides

    def area(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s
