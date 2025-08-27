import re

def user_input():
    string = input("Введите выражение:\n")
    pattern = r"^\d+\s{1}[\+\-\*\/]\s{1}\d+$"

    str_filter = re.fullmatch(pattern, string)

    if str_filter is None:
        raise ValueError("Неверный формат ввода!")
    else:
        return string

def int_filter(number):
    if 1 <= number <= 10:
        return number
    else:
        raise ValueError("Число %s не входит в допустимый диапазон!" % number)

if __name__ == '__main__':
    user_input()