class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

class EmployeeManage:
    def __init__(self):
        self.employee = []
    
    def add_employee(self, emp_id, name):
        self.employee.append(Employee(emp_id, name))
    
    def update_employee(self, emp_id, new_name):
        for emp in self.employee:
            if emp.emp_id == emp_id:
                emp.name = new_name
    
    def delete_employee(self,emp_id):
        for emp in self.employee:
            if emp.emp_id == emp_id:
                self.employee.remove(emp)
                break
    
    def show_all(self):
        for emp in self.employee:
            print(f'Employee ID: {emp.emp_id}, Name: {emp.name}')

manager = EmployeeManage()
print("\n---Add Employee---")
manager.add_employee(1, "Sai")
manager.add_employee(2, "Ranjith")
manager.add_employee(3, "Kalai")
manager.show_all()

print("\n---Update Employee---")
manager.update_employee(2, "Radhika")
manager.show_all()

print("\n---Delete Employee---")
manager.delete_employee(1)
manager.show_all()