def my_func1():
    first_number = int(input('Введите число с которого будет начинаться список: '))
    last_number = int(input('Введите число на котором заканчивается список: '))
    from itertools import count
    for el in count(first_number):
        if el > last_number:
            break
        else:
            print(el)


def my_func2():
    from itertools import cycle
    repeat = int(input('Сколько раз должен повториться список? '))
    my_list = list(range(10, 13))
    my_list_len = len(my_list)
    repeat_list = my_list_len * repeat
    c = 0
    for el in cycle(my_list):
        if c >= repeat_list:
            break
        else:
            print(el)
            c = c + 1

