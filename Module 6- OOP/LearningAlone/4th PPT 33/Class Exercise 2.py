from enum import Enum

class Student:
    def __init__(self, id, name, age, email, course):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.course = course


class Course(Enum):
    AI = 'AI'
    FULLSTACK = 'FullStack'
    QA = 'QA'
    CYBER = 'Cyber'
    PRODUCT_MANAGEMENT = 'Product Management'


student1 = Student(1, 'Shalev', 23, 'shalevch1@gmail.com', Course.AI)
student2 = Student(2, 'Adam', 99, 'adam@gmail.com', Course.QA)
student3 = Student(3, 'Eve', 98, 'eve@gmail.com', Course.PRODUCT_MANAGEMENT)

students = [student1, student2, student3]

course_counts = {course: 0 for course in Course}

for student in students:
    course_counts[student.course] += 1
for course, count in course_counts.items():
    print(f"{course.name}: {count}")