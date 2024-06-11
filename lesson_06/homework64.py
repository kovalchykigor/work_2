import random

lst = [random.randint(1,100) for x in range(20)]
counter = 0
for element in lst:
    if element % 2 == 0:
        counter += element
print(lst, '\n', "Sum of even numbers is: ", counter)