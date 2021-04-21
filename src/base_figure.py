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
        sum_elem = self.area() + figure.area()
        return sum_elem
