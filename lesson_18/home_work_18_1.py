from decorators import log_decorator, error_decorator_for_generator, error_decorator_for_iterator


@log_decorator
@error_decorator_for_iterator
def return_reversed_list_iterator(my_list: list):
    #x = 10 / 0  # ZerroDivisionError
    return iter(reversed(my_list))

my_list = [1, 2, 3, 4, 5]
temp_list = []
for element in return_reversed_list_iterator(my_list):
    temp_list.append(element)
print(temp_list, "\n", "-"*80)


@log_decorator
@error_decorator_for_iterator
def return_even_from_zero_to_n_iterator(n:int):
    #x = 10 / 0  # ZerroDivisionError
    return iter(range(n+1))

result = return_even_from_zero_to_n_iterator(30)
if isinstance(result, str):
    print(result, "\n", "-"*80)
else:
    lst = []
    for element in result:
        lst.append(element)
    print(lst, "\n", "-"*80)



@error_decorator_for_generator
@log_decorator
def return_even_from_zero_to_n_generator(n:int):
    count = 0
    x = 10 / 0  #ZerroDivisionError
    while count <= n:
        yield count
        count += 2

lst_from_zeor_to_n = []
for element in return_even_from_zero_to_n_generator(100):
    lst_from_zeor_to_n.append(element)
print(lst_from_zeor_to_n, "\n", "-"*80)


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

print(result2, "\n", "-"*80)
