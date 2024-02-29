# -*- config: utf8 -*-

def square_number(x):
    return x ** 2


def is_odd(x):
    return x % 2


list_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

odd_squares = map(square_number, filter(is_odd, list_numbers))
print(list(odd_squares))
