import re


def is_palindrome(s):
    """
    Проверяет, является ли строка палиндромом.
    :param s: Входная строка.
    :return: True, если строка палиндром, иначе False.
    """
    # Приведение к нижнему регистру
    s = s.lower()

    # Удаление всех символов, кроме букв и цифр (латиница и кириллица)
    s = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s)

    # Сравнение строки с перевёрнутой копией
    return s == s[::-1]


# Пример использования
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("Hello, World!"))  # False
print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("Привет, мир!"))  # False