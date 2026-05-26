import re
from typing import Callable


def generator_numbers(text: str):
    """Генератор чисел з тексту"""
    
    # Регулярний вираз для пошуку цілих та десяткових чисел
    pattern = r"\b\d+(?:\.\d+)?\b" 

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    """Повертає суму всіх чисел у тексті"""
    
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_profit = sum_profit(text, generator_numbers)

print(f"\nЗагальний дохід: {total_profit}\n")