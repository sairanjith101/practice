# 1.Class to store student details.

class Student:
    def __init__(self, student_id, name, age, gender, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade

    def display_details(self):
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Grade      : {self.grade}")
