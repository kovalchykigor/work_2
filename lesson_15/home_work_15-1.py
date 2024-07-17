from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def get_class_name(self):
        return self.__class__.__name__


class Figure_square(Figure):

    def __init__(self, length_a):
        if not isinstance(length_a, (int, float)) or length_a <= 0:
            raise ValueError("Side length must be a positive number")
        self.__length_a = length_a

    def square(self):
        return f"Square of '{self.get_class_name()}' is: {self.__length_a  * self.__length_a}"

    def perimetr(self):
        return f"Perimetr of '{self.get_class_name()}' is: {self.__length_a * 4}"


class Figure_rectangle(Figure):

    def __init__(self, length_a, length_b):
        if not isinstance(length_a, (int, float)) or length_a <= 0:
            raise ValueError("Side length must be a positive number")
        self.__length_a = length_a

        if not isinstance(length_b, (int, float)) or length_b <= 0:
            raise ValueError("Side length must be a positive number")
        self.__length_b = length_b

    def square(self):
        return f"Square of '{self.get_class_name()}' is: {self.__length_a * self.__length_b}"

    def perimetr(self):
        return f"Perimetr of '{self.get_class_name()}' is: {(self.__length_a + self.__length_b) * 2}"


class Figure_hexagon(Figure):

    def __init__(self, length_a):
        if not isinstance(length_a, (int, float)) or length_a <= 0:
            raise ValueError("Side length must be a positive number")
        self.__length_a = length_a

    def square(self):
        return f"Square of '{self.get_class_name()}' is: {(3 * math.sqrt(3) / 2) * (self.__length_a ** 2)}"

    def perimetr(self):
        return f"Perimetr of '{self.get_class_name()}' is: {self.__length_a * 6}"


figures_list = [
    Figure_square(5),
    Figure_rectangle(2, 3),
    Figure_hexagon(6)
]

print(figures_list)

for figure in figures_list:
    print(figure.square())
    print(figure.perimetr(), "\n")


