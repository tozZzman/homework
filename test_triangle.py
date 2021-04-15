import pytest
from geometric_figures import Rectangle, Triangle

@pytest.fixture()
def figure():
    cls_figure = Triangle(name='Треугольник', sides=[2, 2, 3])
    return cls_figure

def test_triangle_area(figure):
    assert figure.area() == 1.984313483298443, "Неверная площадь треугольника"

def test_triangle_perimeter(figure):
    assert figure.perimeter() == 7, "Неверный периметр треугольника"

def test_triangle_add_area(figure):
    s = figure.add_area(Rectangle(name='Прямоугольник', sides=[4, 2, 2, 4]))
    assert s == 9.984313483298443, "Неверная суммарная площадь"

@pytest.mark.parametrize('sides', [[[2, 2, 4], 'У треугольника сумма длин двух любых сторон больше длины оставшейся стороны'],
                                   [[2, 2, 4, 4], 'У треугольника должно быть три стороны!'],
                                   [[2, 1], 'У треугольника должно быть три стороны!']])
def test_triangle_wrong_sides(sides):
    try:
        Triangle(name='Треугольник', sides=sides[0])
        raise Exception(f'Ожидалаь ошибка: {sides[1]}')
    except Exception as er:
        assert sides[1] == er.__str__(), "Исключение не сходится ожидаемым"



