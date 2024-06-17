def the_sum_of_element_values_1(lst: list):
    print("func 1")
    for element in lst:
        split_list = element.split(",")
        int_list = []
        for value in split_list:
            int_list.append(int(value))
        print(f"{int_list} sum = {sum(int_list)}")


def the_sum_of_element_values_2(lst: list):
    print("func 2")
    for element in lst:
        result = [int(value) for value in element.split(",")]
        print(f"{result} sum = {sum(result)}")


list_1 = ["1,2,3,4", "1,2,3,4,50"]
list_2 = ["1,2,3,4", "1,2,3,4,50", "1,2,3,qwerty"]

try:
    the_sum_of_element_values_1(list_1)
    the_sum_of_element_values_2(list_2)

except Exception as e:
    print(f"I can't do this because of: {e}")
