import unittest
from vowels import count_vowels


class TestCountVowels(unittest.TestCase):

    def test_ukrainian_letters(self):
        """Перевірка рядка з українськими літерами."""
        self.assertEqual(count_vowels("Привіт, Світ!"), 3)  # и, і, і
        self.assertEqual(count_vowels("Яблуко"), 3)          # Я, у, о

    def test_empty_string(self):
        """Перевірка порожнього рядка."""
        self.assertEqual(count_vowels(""), 0)

    def test_digits_and_symbols(self):
        """Перевірка рядка з цифрами та спецсимволами."""
        self.assertEqual(count_vowels("1234567890!@#$%^&*()"), 0)
        self.assertEqual(count_vowels("Тест 123!"), 1)      # е

    def test_invalid_type(self):
        """Перевірка генерації TypeError при передачі не-рядка."""
        with self.assertRaises(TypeError):
            count_vowels(123)


if __name__ == "__main__":
    unittest.main()