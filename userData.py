import re
import sys


def user_input():
    string = input("Введите выражение:\n")
    pattern = r"^\d+\s{1}[\+\-\*\/]\s{1}\d+$"

    str_filter = re.fullmatch(pattern, string)

    if str_filter is None:
        print("Неверный формат ввода!")
        sys.exit(1)
    else:
        return string

def int_filter(number):
    if 1 <= number <= 10:
        return number
    else:
        print("Число %s не входит в допустимый диапазон!" % number)
        sys.exit(2)

if __name__ == '__main__':
    user_input()