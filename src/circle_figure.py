import math
from .base_figure import Figure


class Circle(Figure):
    def __init__(self, name, radius: int):
        super().__init__(name, sides=[], angles=0)
        self.radius = radius

    def perimeter(self):
        p = 2 * math.pi * self.radius
        return p

    def area(self):
        s = math.pi * self.radius ** 2
        return s
