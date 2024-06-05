adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("#### task 01", "\n")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer, "\n")

# task 02 ==
""" Замініть .... на пробіл
"""
print("#### task 02", "\n")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", "")
print(adwentures_of_tom_sawer, "\n")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("#### task 03", "\n")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
split_to_list = adwentures_of_tom_sawer # для слідуючих завдань
adwentures_of_tom_sawer = ' '.join(split_to_list)
print(adwentures_of_tom_sawer, "\n")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("#### task 04", "\n")
result_04 = adwentures_of_tom_sawer.count('h')
print("The letter 'h' is found in the text ", result_04, " times", "\n")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("#### task 05", "\n")
count = 0
for word in split_to_list:
    if word[0].isupper():
        count += 1
print("Count of words that starts with upper case is: ", count, "\n")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("#### task 06", "\n")
first_find = adwentures_of_tom_sawer.find("Tom")
second_find = adwentures_of_tom_sawer.find("Tom", first_find + 1)
print("The index of second find of 'Tom' is: ", second_find, "\n")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("#### task 07", "\n")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences, "\n")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("#### task 08", "\n")
print(adwentures_of_tom_sawer_sentences[3].lower(), "\n")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("#### task 09", "\n")
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith(" By the time"):
        print("The following sentenсe starts with 'By the time' fraze: ", "\n", sentenсe, "\n")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("#### task 10", "\n")
result = len(adwentures_of_tom_sawer_sentences[-2].split())
print("Number of words in the last sentence is: ", result)