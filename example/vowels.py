def count_vowels(text: str) -> int:
    """Рахує кількість голосних літер (українських та англійських) у рядку."""
    if not isinstance(text, str):
        raise TypeError("Переданий аргумент має бути рядком")
    
    vowels = set("аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU")
    return sum(1 for char in text if char in vowels)