import pytest
from src.square_figure import Square
from src.rectangle_figure import Rectangle


@pytest.fixture()
def figure():
    cls_figure = Rectangle(name='Прямоугольник', sides=[2, 2, 4, 4])
    return cls_figure


def test_rectangle_area(figure):
    assert figure.area() == 8, "Неверная площадь прямоугольника"


def test_rectangle_perimeter(figure):
    assert figure.perimeter() == 12, "Неверный периметр прямоугольника"


def test_rectangle_add_area(figure):
    s = figure.add_area(Square(name='Квадрат', sides=[2, 2, 2, 2]))
    assert s == 12, "Неверная суммарная площадь"


@pytest.mark.parametrize('sides', [[[2, 2, 4], 'У прямоугольника должно быть четыре стороны!'],
                                   [[2, 2, 4, 4, 4], 'У прямоугольника должно быть четыре стороны!'],
                                   [[2, 1, 4, 4], 'У прямоугольника параллельные стороны должны быть равны']])
def test_rectangle_wrong_sides(sides):
    try:
        Rectangle(name='Прямоугольник', sides=sides[0])
        raise Exception(f'Ожидалаь ошибка: {sides[1]}')
    except Exception as er:
        assert sides[1] == er.__str__(), "Исключение не сходится ожидаемым"


@pytest.fixture()
def wrong_class():
    class Book:
        def __init__(self):
            pass

    cls = Book
    return cls


def test_rectangle_add_area_error(figure, wrong_class):
    try:
        figure.add_area(wrong_class)
    except Exception as er:
        assert 'Переданный объект не является фигурой' == er.__str__(), "Исключение не сходится ожидаемым"
