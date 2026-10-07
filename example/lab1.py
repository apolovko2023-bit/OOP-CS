def process_positive_number(val) -> float:
    """Перевіряє, чи є значення додатним числом."""
    if not isinstance(val, (int, float)):
        raise TypeError("Аргумент має бути числом!")
    if val <= 0:
        raise ValueError("Число має бути більшим за нуль!")
    
    # Внутрішня перевірка інваріанта
    assert val > 0, "Критична помилка: число від'ємне або дорівнює нулю!"
    return float(val)


# --- Демонстрація роботи ---
if __name__ == "__main__":
    # 1. Правильне введення
    try:
        result = process_positive_number(10.5)
        print(f"Успіх (10.5): {result}")
    except (ValueError, TypeError, AssertionError) as e:
        print(f"Помилка: {e}")

    # 2. Неправильне введення (від'ємне число)
    try:
        process_positive_number(-5)
    except ValueError as e:
        print(f"Перехоплено ValueError (-5): {e}")

    # 3. Неправильний тип даних
    try:
        process_positive_number("abc")
    except TypeError as e:
        print(f"Перехоплено TypeError ('abc'): {e}")