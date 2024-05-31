
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
                       '"That depends a good deal on where you want to get to," said the Cat.\n' \
                       '"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n' \
                       '"—— so long as I get somewhere," Alice added as an explanation.\n' \
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland, "\n")
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("---task 04")
black_sea = 436482
azov_sea = 37800

def square(param_a, param_b):
    return param_a + param_b

print("Square of Azov and Black sea is:", square(black_sea, azov_sea), "\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_goods = 375291
goods_on_store_1_and_store_2 = 250449
goods_on_store_2_and_store_3 = 222950


store_3 = all_goods - goods_on_store_1_and_store_2
store_2 = goods_on_store_2_and_store_3 - store_3
store_1 = goods_on_store_1_and_store_2 - store_2

print("----task 05")
print(" Store 1 = ", store_1, "\n", "Store 2 = ", store_2, "\n", "Store 3 = ", store_3, "\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("----task 06")
months = 18
price_per_month = 1179
result = price_per_month * months

print("Total price of computer is:", result, "\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("----Task 07")
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(" a) ", a, "\n b) ", b, "\n c) ", c, "\n d) ", d, "\n e) ", e, "\n f) ", f, "\n")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("----task 08")
pizza_big = 4 * 274
pizza_middle = 2 * 218
juice = 4 * 35
pie = 1 * 350
water = 3 * 21
result = sum([pizza_big, pizza_middle, juice, pie, water])
print("Number of required money is:", result, "\n")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("----task 09")
all_photos = 232
max_photos_on_page = 8
result = all_photos/max_photos_on_page
print("Number of required pages is:", result, "\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("----task 10")
distance = 1600
fuel_consumption = 9
tank_capacity = 48

total_liters_for_journey = fuel_consumption / 100 * distance
kilometers_on_tank = tank_capacity / fuel_consumption * 100
number_of_tank_fillings = distance / kilometers_on_tank

print(" Liters on full journey: ", total_liters_for_journey, "\n", "Number of tank filings: ", number_of_tank_fillings)