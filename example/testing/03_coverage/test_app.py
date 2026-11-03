
import pytest
from app import Shape


def test_triangle_angles():
    shape = Shape("triangle")
    assert shape.get_angles == (60, 60, 60)


def test_square_angles():
    shape = Shape("square")
    assert shape.get_angles == (90, 90, 90, 90)


def test_rectangle_angles():
    shape = Shape("rectangle")
    assert shape.get_angles == (90, 90, 90, 90)


def test_invalid_shape():
    shape = Shape("circle")
    with pytest.raises(ValueError):
        shape.get_angles

def test_with_assert():
    shape = Shape("triangle")
    assert shape.get_angles == (60, 60, 60)