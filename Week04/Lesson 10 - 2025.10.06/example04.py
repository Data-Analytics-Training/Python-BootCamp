"""
Attributes
Instance attributes: defined with self; they are unique to each object
Class attributes: defined at the class level and shared by all objects
"""


class Car:
    wheel_number = 4  # class attribute


class Student:
    course = "Python 80-hour Bootcamp"
    faculty = ""


print(Car.wheel_number)  # 4
print(Student.course)  # Python 80-hour Bootcamp

student1 = Student()
print(student1.course)  # Python 80-hour Bootcamp

student1.faculty = "Engineering Faculty"
print(Student.faculty)  #     (empty line)
print(student1.faculty)  # Engineering Faculty
