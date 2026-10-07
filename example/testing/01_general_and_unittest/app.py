class Figure:
    VALID_TYPES = {"квадрат", "прямокутник", "трикутник"}

    def __init__(self, figure_type: str, length: float):
        figure_type_clean = figure_type.lower().strip()
        if figure_type_clean not in self.VALID_TYPES:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")
        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль!")

        self.figure_type = figure_type_clean
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.figure_type

    @property
    def get_figure_length(self) -> float:
        # Виправлена реалізація (помилка була у поверненні некоректного атрибута / типу)
        return float(self.length)

    def get_angles(self) -> int:
        """Повертає кількість кутів для фігури."""
        angles_map = {
            "квадрат": 4,
            "прямокутник": 4,
            "трикутник": 3,
        }
        return angles_map[self.figure_type]


def ask_user_and_create_figure() -> Figure:
    """Функція з запитом введення від користувача."""
    fig_type = input("Введіть тип фігури: ")
    length_str = input("Введіть довжину: ")
    return Figure(fig_type, float(length_str))

# Помилковий код у app.py
@property
def get_figure_length(self) -> float:
    return str(self.length)  # Повертав рядок замість числа або некоректне значення