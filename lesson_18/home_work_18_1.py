from decorators import log_decorator, error_decorator_for_generator, error_decorator_for_iterator


@log_decorator
@error_decorator_for_iterator
def return_reversed_list_iterator(my_list: list):
    x = 10 / 0  # ZerroDivisionError
    my_iterable = iter(reversed(my_list))
    temp_list = []
    for element in my_iterable:
        temp_list.append(element)
    return temp_list

my_list = [1, 2, 3, 4, 5]
return_reversed_list_iterator(my_list)


@log_decorator
@error_decorator_for_iterator
def return_even_from_zero_to_n_iterator(n:int):
    x = 10 / 0  # ZerroDivisionError
    my_iter = iter(range(n+1))
    lst = []
    for element in my_iter:
        if element % 2 == 0 and element != 0:
            lst.append(element)
    return lst

return_even_from_zero_to_n_iterator(22)


@error_decorator_for_generator
@log_decorator
def return_even_from_zero_to_n_generator(n:int):
    count = 0
    x = 10 / 0  #ZerroDivisionError
    while count <= n:
        yield count
        count += 2

for element in return_even_from_zero_to_n_generator(100):
    print(element)


@error_decorator_for_generator
@log_decorator
def fibonacci_generator(n:int):
    a, b = 0, 1
    x = 10 / 0 #ZerroDivisionError
    while a <= n:
        yield a
        a, b = b, a + b

result2 = []
for element in fibonacci_generator(15):
    result2.append(element)
    print(result2)
