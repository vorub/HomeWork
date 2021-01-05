def my_func():
    from sys import argv
    name = argv
    hours = argv
    payment = argv
    prize = argv
    hours = int(hours)
    payment = int(payment)
    prize = int(prize)
    salary = hours * payment + prize
    print(f'Зарплата: {salary}')


