from .base_figure import Figure


class Rectangle(Figure):
    def __init__(self, name, sides):
        super().__init__(name, sides, angles=4)

        if len(sides) != 4:
            raise Exception('У прямоугольника должно быть четыре стороны!')
        elif sides.count(sides[0]) != 2 or sides.count(sides[1]) != 2 \
                or sides.count(sides[2]) != 2 or sides.count(sides[3]) != 2:
            raise Exception('У прямоугольника параллельные стороны должны быть равны')
        self.sides = sides

    def area(self):
        a = self.sides[0]
        b = None
        for i in range(len(self.sides)):
            if self.sides[i] != a:
                b = self.sides[i]
                break
        return a * b
