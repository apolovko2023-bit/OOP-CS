import pytest
from app import Figure

FIGURES = ["квадрат", "прямокутник", "трикутник"]


# ---------- Базові тести ----------
@pytest.mark.unit
def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.figure_type == "трикутник"


def test_invalid_length():
    with pytest.raises(ValueError):
        Figure("квадрат", 0)


# ---------- ⭐ Параметризований тест для всіх фігур ----------
@pytest.mark.unit
@pytest.mark.parametrize("figure", FIGURES)
def test_allowed_figure(figure):
    assert Figure(figure, 1).figure_type == figure


# ---------- ⭐ Fixture з довжиною 10 ----------
@pytest.fixture
def length():
    return 10


@pytest.fixture
def square(length):
    return Figure("квадрат", length)


def test_square_length(square):
    assert square.get_figure_length == 999   # зламано навмисно


def test_square_type(square):
    assert square.figure_type == "квадрат"


# ---------- 🔥 Неправильні типи та значення ----------
@pytest.mark.parametrize("bad_length", [0, -1, -100])
def test_invalid_length_value(bad_length):
    with pytest.raises(ValueError):
        Figure("квадрат", bad_length)


@pytest.mark.parametrize("bad_length", ["10", None, [5]])
def test_invalid_length_type(bad_length):
    with pytest.raises(TypeError):
        Figure("квадрат", bad_length)


@pytest.mark.parametrize("bad_figure", ["ромб", ""])
def test_invalid_figure_value(bad_figure):
    with pytest.raises(ValueError):
        Figure(bad_figure, 5)


@pytest.mark.parametrize("bad_figure", [123, None])
def test_invalid_figure_type(bad_figure):
    with pytest.raises(AttributeError):
        Figure(bad_figure, 5)


# ---------- ⭐ Fixture зі scope="module" ----------
@pytest.fixture(scope="module")
def allowed_figures():
    return FIGURES


def test_figures_not_empty(allowed_figures):
    assert len(allowed_figures) > 0


def test_triangle_in_figures(allowed_figures):
    assert "трикутник" in allowed_figures