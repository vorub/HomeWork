number_list = [1, 2, 5, 1, 77, 5, 100]
new_list = [el for number, el in enumerate(number_list) if number_list[number] > number_list[number - 1]]
print(new_list)
