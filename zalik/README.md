# ЗАЛІК  
## Завдання №3

### Інформація про студента
- **Виконала:** Аліна Половко  
- **Група:** КН-33  

### Умова завдання
Створити клас `FactorialCalculator`, який:

- Приймає в конструкторі додатне число `n`
- Має метод `calculate()`, який обчислює факторіал числа
- Має property `factorial`, яка повертає обчислений факторіал
- Містить метод `__str__`, що виводить ім’я та групу студента
- У циклі створює 3 об’єкти класу з різними значеннями `n`

### Реалізація на Python

```python
class FactorialCalculator:
    """Клас для обчислення факторіалу числа"""

    # Інформація про студента
    student_name = "Аліна Половко"
    student_group = "КН-33"

    def __init__(self, n):
        """Конструктор приймає додатне число n"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("n має бути невід'ємним цілим числом")
        self.n = n
        self._factorial = None

    def calculate(self):
        """Обчислює факторіал числа n"""
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        self._factorial = result
        return self._factorial

    @property
    def factorial(self):
        """Property для повернення обчисленого факторіалу"""
        if self._factorial is None:
            self.calculate()
        return self._factorial

    def __str__(self):
        """Метод для виведення інформації про студента"""
        return f"Студентка: {self.student_name}, Група: {self.student_group}"


# Демонстрація роботи класу
print("=" * 50)
print("Демонстрація роботи класу FactorialCalculator")
print("=" * 50)

numbers = [5, 7, 10]

for index, n in enumerate(numbers, start=1):
    calc = FactorialCalculator(n)
    print(f"\nОб'єкт {index}: {calc}")
    print(f"Факторіал числа {n} = {calc.factorial}")

print("\n" + "=" * 50)
