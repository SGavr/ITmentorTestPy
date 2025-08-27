import sys
from userData import user_input, int_filter
from calculation import calc_operation

def main(input: str) -> str:
    data_array = str.split(" ")
    data_array[0] = int(data_array[0])
    data_array[2] = int(data_array[2])

    int_filter(data_array[0])
    int_filter(data_array[2])

    return calc_operation(data_array[0], data_array[1], data_array[2])

try:
    str = user_input()
    result = main(str)
except ValueError as e:
    print(e)
    sys.exit(1)

print(result)