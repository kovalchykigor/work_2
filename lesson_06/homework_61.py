
user_chars = input("Please input random sequence of chars:\n")
unic_chars = set(user_chars)

count_of_chars = len(unic_chars)
print('Count of chars =', count_of_chars)
if count_of_chars > 10:
    print(True)
else:
    print(False)