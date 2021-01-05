
def fact():
    from math import factorial
    from itertools import count
    for el in count(1):
        yield factorial(el)

answer = fact()
x = 0
user_number = int(input('Введите до какого числа нужно считать факториал: '))
for i in answer:
    if x <= user_number - 1:
        print(i)
        x += 1
    else:
        break



