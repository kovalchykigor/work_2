
def count_unique_characters(user_chars):
    unic_chars = set(user_chars)
    count_of_chars = len(unic_chars)

    return count_of_chars, count_of_chars > 10

def count_uppercase_starting_words(text):
    count = 0
    split_to_list = text.split()
    for word in split_to_list:
        if word[0].isupper():
            count += 1
    return count

def extract_strings(lst1):
    lst2 = []
    for element in lst1:
        if isinstance(element, str):
            lst2.append(element)
    return lst2
