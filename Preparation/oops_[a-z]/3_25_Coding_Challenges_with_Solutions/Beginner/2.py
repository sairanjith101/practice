# 2.Implement a counter using static/class variable.

class Student:
    count = 0  # Class variable (static) to track number of instances

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        Student.count += 1  # Increment counter whenever a new object is created

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}")

    @classmethod
    def get_count(cls):
        return cls.count

    
s1 = Student("S101", "Arjun")
s2 = Student("S102", "Meera")
s3 = Student("S103", "Ravi")

print("Total Students Created:", Student.get_count())
