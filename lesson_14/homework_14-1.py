class Student:

    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade


student = Student("Igor", "Kovalchuk", 36, 5)
print(student.first_name, student.last_name, student.age, student.average_grade)

student.set_average_grade(-5)
print(student.first_name, student.last_name, student.age, student.average_grade)
