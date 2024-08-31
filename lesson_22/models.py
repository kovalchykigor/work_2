from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Асоціативна таблиця для зв'язку "багато до багатьох"
student_course_association = Table(
    'student_course_association', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    age = Column(Integer)

    courses = relationship('Course', secondary=student_course_association, back_populates='students')


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    course_name = Column(String)

    students = relationship('Student', secondary=student_course_association, back_populates='courses')
