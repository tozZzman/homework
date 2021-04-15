import math


class Figure:
    def __init__(self, name: str, sides: list, angles: int):
        self.name = name
        self.angles = angles
        self.sides = sides

    def __new__(cls, *args, **kwargs):
        if cls is Figure:
            raise Exception('Запрещено создавать инстансы базового класса')
        else:
            return object.__new__(cls)

    def perimeter(self):
        return sum(self.sides)

    def add_area(self, figure: object):
        if isinstance(figure, Figure) is not True:
            raise Exception('Переданный объект не является фигурой')
        sum = self.area() + figure.area()
        return sum


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
        p = (a + b + c)/2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s


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
        i = 1
        b = None
        for i in range(len(self.sides)):
            if self.sides[i] != a:
                b = self.sides[i]
                break
        return a * b


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


class Circle(Figure):
    def __init__(self, name, radius: int):
        super().__init__(name, sides=[], angles=0)
        self.radius = radius

    def perimeter(self):
        p = 2 * math.pi * self.radius
        return p

    def area(self):
        s = math.pi * self.radius**2
        return s


