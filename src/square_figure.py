from .base_figure import Figure


class Square(Figure):
    def __init__(self, name, sides):
        super().__init__(name, sides, angles=4)

        if len(sides) != 4:
            raise Exception('У квадрата должно быть четыре стороны!')
        elif sides.count(sides[0]) != 4:
            raise Exception('У квадрата все стороны должно быть равны!')
        self.sides = sides

    def area(self):
        a = self.sides[0]
        b = self.sides[1]
        return a * b
