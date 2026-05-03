def safe_divide(a: float, b: float) -> dict:
    """
    Ділить два числа з перевіркою на нуль.

    Args:
        a (float): ділене
        b (float): дільник

    Returns:
        dict: результат або помилка
    """
    if b == 0:
        return {
            "result": None,
            "error": "Ділення на нуль неможливе"
        }

    return {
        "result": a / b,
        "error": None
    }


def count_words(text: str) -> dict:
    """
    Рахує кількість слів у тексті.
    """
    if not text:
        return {"result": 0, "error": "Порожній текст"}

    words = len(text.split())
    return {"result": words, "error": None}