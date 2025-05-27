


class Student:
    def __init__(self, name, age, class_level, avg_grades, course):
        self.age = age
        self.name = name
        self.class_level = class_level
        self.avg_grades = avg_grades
        self.course = course

    def print_info(self):
        print(f"The student {self.name} is {self.age} years old. Learning {self.course} course at level {self.class_level}. His average grades is {self.avg_grades}")

class Course:
    def __init__(self, course_name, course_size = 0):
        self.course_name = course_name
        self.course_size = course_size
        self.student_list = []

    def register_student(self, student):
        if len(self.student_list) < self.course_size:
            self.student_list.append(student)
            print(f"{student.name} added. {self.course_name} has {len(self.student_list)} students.\n The course has {self.course_size - len(self.student_list)} spots left.")
        else:
            print(f"Course size exceeded the limit! ({self.course_size} - limit)")

    def print_students(self):
        for student in self.student_list:
            student.print_info()

python_course = Course("Python Programming", 2)
student1 = Student("Alice", 17, "11th Grade", 88, "Python Programming")
student2 = Student("Bob", 18, "12th Grade", 91, "Python Programming")
student3 = Student("Charlie", 16, "10th Grade", 85, "Python Programming")

python_course.register_student(student1)
python_course.register_student(student2)
python_course.register_student(student3)

python_course.print_students()
