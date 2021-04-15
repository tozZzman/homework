import pytest
from geometric_figures import Circle, Square

@pytest.fixture()
def figure():
    cls_figure = Circle(name='Круг', radius=5)
    return cls_figure

def test_circle_area(figure):
    assert figure.area() == 78.53981633974483, 'Неверная площадь круга'

def test_circle_perimeter(figure):
    assert figure.perimeter() == 31.41592653589793, 'Неверный периметр круга'

def test_circle_add_area(figure):
    s = figure.add_area(Square(name='Квадрат', sides=[2, 2, 2, 2]))
    assert s == 82.53981633974483, 'Неверная суммарная площадь фигур'