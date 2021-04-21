import pytest
from src.triangle_figure import Triangle
from src.square_figure import Square


@pytest.fixture()
def figure():
    cls_figure = Square(name='Квадрат', sides=[3, 3, 3, 3])
    return cls_figure


def test_square_area(figure):
    assert figure.area() == 9, 'Неверная площадь квадрата'


def test_square_perimeter(figure):
    assert figure.perimeter() == 12, 'Неверный периметр квадрата'


def test_square_add_area(figure):
    s = figure.add_area(Triangle(name='Треугольник', sides=[2, 2, 2]))
    assert s == 10.732050807568877, 'Неверная суммарная площадь фигур'


@pytest.mark.parametrize('sides', [[[3, 3, 3], 'У квадрата должно быть четыре стороны!'],
                                   [[3, 3, 3, 4], 'У квадрата все стороны должно быть равны!']
                                   ])
def test_square_invalid_sides(sides):
    try:
        Square(name='Квадрат', sides=sides[0])
    except Exception as er:
        assert sides[1] == er.__str__(), 'Неверная ошибка'
