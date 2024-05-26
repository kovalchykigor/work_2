# task 01 == Виправте синтаксичні помилки

print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки

hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print

for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук

apples = 2
banana = apples * 4
print(apples)


# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача

perimeter = storona_1 + storona_2 + storona_3 + storona_4
print("Perimeter = ", perimeter, "\n")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print("-----Task 07")
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
result = apple_tree + pear_tree + plum_tree
output = f' All treas:\n {apple_tree} apple tree + {plum_tree} plum tree + {pear_tree} pear tree = {result} trees'
print(output, "\n")
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("-----Task 08")
result = f'AM temperature = {0 + 5}, PM temperature = {5 - 10}, Evening temperature = {-5 + 4}'
print(result, "\n")
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("-----Task 09")
boys = 24
girls = boys/2
all_kids = boys + girls
result = all_kids - 1 - 2
print("Current number of children = ", result, "\n")
"""ЗАДАЧА СФОРМУЛЬОВАНА НЕ ТОЧНО, ТОМУ ЩО НЕ СКАЗАТО ЩО ХЛОПЧИК ЩО ЗАХВОРІВ НЕ ПРИЙШОВ"""

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("-----Task 10")
first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price)/2
result = first_book_price + second_book_price + third_book_price
print("All books price is ", result, "\n")