import unittest
from unittest.mock import patch
from app import Figure, ask_user_and_create_figure


class TestFigure(unittest.TestCase):

    def setUp(self):
        self.square = Figure("квадрат", 5)
        self.rectangle = Figure("прямокутник", 10)
        self.triangle = Figure("трикутник", 3)

    def test_figure_type(self):
        self.assertEqual(self.square.get_figure_type, "квадрат")

    def test_figure_length(self):
        # Перевірка довжини
        self.assertEqual(self.square.get_figure_length, 5.0)
        self.assertEqual(self.rectangle.get_figure_length, 10.0)

    def test_get_angles(self):
        """Перевірка кількості кутів."""
        self.assertEqual(self.square.get_angles(), 4)
        self.assertEqual(self.rectangle.get_angles(), 4)
        self.assertEqual(self.triangle.get_angles(), 3)

    def test_invalid_length(self):
        """Тести для нульової та від'ємної довжини."""
        with self.assertRaises(ValueError):
            Figure("квадрат", 0)
        with self.assertRaises(ValueError):
            Figure("квадрат", -5)

    def test_unknown_figure_type(self):
        """Тест для невідомого типу фігури."""
        with self.assertRaises(ValueError):
            Figure("коло", 5)

    def test_subtest_all_figures(self):
        """Параметризований тест за допомогою subTest."""
        test_cases = [
            ("квадрат", 4, 4),
            ("прямокутник", 8, 4),
            ("трикутник", 6, 3),
        ]
        for f_type, length, expected_angles in test_cases:
            with self.subTest(figure_type=f_type, length=length):
                fig = Figure(f_type, length)
                self.assertEqual(fig.get_figure_length, length)
                self.assertEqual(fig.get_angles(), expected_angles)

    @patch("builtins.input", side_effect=["квадрат", "7"])
    def test_ask_user_and_create_figure(self, mock_input):
        """Тестування інтерактивної функції за допомогою mock.patch."""
        figure = ask_user_and_create_figure()
        
        self.assertEqual(figure.get_figure_type, "квадрат")
        self.assertEqual(figure.get_figure_length, 7.0)
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()