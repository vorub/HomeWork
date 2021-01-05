my_list = list(range(100, 1000))
new_list = [el for el in my_list if el % 2 == 0]
print(f'Список четных чисел: {new_list}')
from functools import reduce
print(reduce(lambda x, y: x*y, new_list))