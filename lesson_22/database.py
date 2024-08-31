import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course
from faker import Faker
import random

DATABASE_URL = "sqlite:///E:/GoIT/Hilel.db"

# Видалення старої бази даних
if os.path.exists("E:/GoIT/Hilel.db"):
    os.remove("E:/GoIT/Hilel.db")

engine = create_engine(DATABASE_URL, echo=True)

# Створення всіх таблиць
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Створення 20 студентів
faker = Faker()
students = []
for _ in range(20):
    new_student = Student(full_name=faker.name(), age=random.randint(18, 25))
    students.append(new_student)
    session.add(new_student)
session.commit()

# Створення 5 курсів
course_list = ['Course_1', 'Course_2', 'Course_3', 'Course_4', 'Course_5']
courses = []
for course_name in course_list:
    new_course = Course(course_name=course_name)
    courses.append(new_course)
    session.add(new_course)
session.commit()

# Призначення студентам випадкових курсів
for student in students:
    student_courses = random.sample(courses, k=random.randint(1, 3))
    student.courses.extend(student_courses)
    session.add(student)
session.commit()
