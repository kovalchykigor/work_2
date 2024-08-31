from models import Student, Course
from sqlalchemy.orm import sessionmaker
from database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_students_for_course(course_name):
    course = session.query(Course).filter(Course.course_name == course_name).first()
    if course:
        return course.students
    return []

def get_courses_for_student(student_name):
    student = session.query(Student).filter(Student.full_name == student_name).first()
    if student:
        return student.courses
    return []

def update_student(student_id, new_full_name=None, new_age=None):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        if new_full_name:
            student.full_name = new_full_name
        if new_age:
            student.age = new_age
        session.commit()
        print("-"*80, f'\nStudent {student_id} updated successfully.\n', "-"*80)
    else:
        print("-"*80, f'\nStudent with id {student_id} not found.\n', "-"*80)

def update_course(course_id, new_course_name=None):
    course = session.query(Course).filter(Course.id == course_id).first()
    if course:
        if new_course_name:
            course.course_name = new_course_name
        session.commit()
        print("-"*80, f'\nCourse {course_id} updated successfully.\n', "-"*80)
    else:
        print("-"*80, f'\nCourse with id {course_id} not found.\n', "-"*80)

def delete_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("-"*80, f'\nStudent {student_id} deleted successfully.\n', "-"*80)
    else:
        print("-"*80, f'\nStudent with id {student_id} not found.\n', "-"*80)
