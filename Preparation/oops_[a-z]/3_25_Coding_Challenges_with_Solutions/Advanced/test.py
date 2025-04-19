class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name):
        self.employees.append(Employee(emp_id, name))
    
    def update_employee(self, emp_id, new_name):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.name = new_name
    
    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                break
    
    def show_all(self):
        for emp in self.employees:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}")

manager = EmployeeManager()
manager.add_employee(1, "Sai")
manager.add_employee(2, "Ranjith")
manager.add_employee(3, "Kalai")
manager.update_employee(2, "Radhika")
manager.show_all()
print("\n--After Delete--")
manager.delete_employee(2)
manager.show_all()