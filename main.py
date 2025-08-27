from userData import *
from calculation import *

data = user_input()

data_array = data.split(" ")
data_array[0] = int(data_array[0])
data_array[2] = int(data_array[2])

int_filter(data_array[0])
int_filter(data_array[2])

print(calc_operation(data_array[0], data_array[1], data_array[2]))