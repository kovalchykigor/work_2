import random
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    dobutok = 25
    multiplier = 1
    result = 0
    # Complete the while loop condition.
    while result < dobutok:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
    print('')

print("-----Task 1")
multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("-----Task 2")
def sum_of_two(a, b):
    return a + b
print(sum_of_two(1,3), '\n')

# task 3
print("-----Task 3")
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(lst:list):
   return sum([number for number in lst])/len(lst)

lst = [random.randint(1,3) for x in range(5)]
print(lst, '\n', "Arithmetic_mean is:", arithmetic_mean(lst), '\n')

# task 4
print("-----Task 4")
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(chars:str):
    return chars[::-1]

chars = "Hello"
print(reverse_string(chars), '\n')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("-----Task 5")

def the_longest_word_in_the_list(lst:list):
    length_of_each_word_list = []

    for element in lst:
        length_of_each_word_list.append(len(element))

    print(length_of_each_word_list)
    max_symbols = max(length_of_each_word_list)
    print(f"The max length of word in the list is '{max_symbols}' symbols")

    for index, value in enumerate(length_of_each_word_list):
        if value == max_symbols:
            print(f"The longest word in the list is: '{lst[index]}'", '\n')

some_list_1 = ["написати", "функцію", "яка", "приймає", "список", "слів", "та", "повертає", "найдовше", "слово", "у", "списку"]
some_list_2 = ["Написати", "функцію", "яка", "приймає", "рядок", "та", "повертає", "його", "у", "зворотному", "порядку"]
the_longest_word_in_the_list(some_list_2)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("-----Task 6")
def find_substring(str1, str2):
    if str2 in str1:
        index = str1.index(str2[0])
        return index
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2), '\n') # поверне -1

# task 7
print("-----Task 7")
def append_string_items(lst1, lst2):
    for element in lst1:
        if isinstance(element, str):
            lst2.append(element)
    return (lst1, lst2)

data_list, result = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'], []
print(append_string_items(data_list, result), '\n')

# task 8
print("-----Task 8")
def wait_for_the_letter(str1:str, str2:str):
    user_input = ""
    while str1 not in user_input and str2 not in user_input:
        print(f"Please input {str1} or {str2}")
        user_input = input()

    return "Thank you!"
print(wait_for_the_letter("k", 'K'), '\n')

# task 9
print("-----Task 9")
def count_unique_symbols_in_string(user_chars):
    unic_chars = set(user_chars)
    count_of_chars = len(unic_chars)
    print('Count of chars =', count_of_chars)
    if count_of_chars > 10:
        return True
    else:
        return False

print(count_unique_symbols_in_string(input("Please input random sequence of chars:\n")), '\n')

# task 10
print("-----Task 10")
def sum_of_even_nums_in_string(lst):
    counter = 0
    for element in lst:
        if element % 2 == 0:
            counter += element
    return f"{lst} '\n' Sum of even numbers is: {counter}"

random_list = [random.randint(1, 100) for x in range(20)]
print(sum_of_even_nums_in_string(random_list))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""