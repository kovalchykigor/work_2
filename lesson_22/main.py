from queries import get_students_for_course, get_courses_for_student, update_student, update_course, delete_student
from database import students

# Отримання студентів для курсу
students_for_course = get_students_for_course('Course_1')
for student in students_for_course:
    print("-"*80, f'\nStudent Name: {student.full_name}, Age: {student.age}\n', "-"*80)

# Отримання курсів для студента
student_name = students[1].full_name
courses_for_student = get_courses_for_student(student_name)
for course in courses_for_student:
    print("-"*80, f"\nStudent Name: '{student_name}' Course Name: '{course.course_name}'\n", "-"*80)

# Оновлення даних студента
update_student(1, new_full_name='Updated Name', new_age=100)

# Оновлення даних курсу
update_course(1, new_course_name='Updated Course Name')

# Видалення студента
delete_student(2)
