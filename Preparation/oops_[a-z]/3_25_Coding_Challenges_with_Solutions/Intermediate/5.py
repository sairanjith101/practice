# ✅ Multiple Inheritance Demo – Python Code

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, emp_id, department):
        self.emp_id = emp_id
        self.department = department

    def show_employee_info(self):
        print(f"Employee ID: {self.emp_id}, Department: {self.department}")

class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, department, team_size):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, department)
        self.team_size = team_size

    def show_manager_info(self):
        print("\n---Manager Details---")
        self.show_person_info()
        self.show_employee_info()
        print(f"Team Size: {self.team_size}")

m = Manager("Sai", 29, "123", "IT", 10)
m.show_manager_info()