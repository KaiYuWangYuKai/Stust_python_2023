class Employee :
    def __init__(self , emp_name , emp_id , emp_salary , emp_department):
        self.emp_name = emp_name            
        self.emp_id = emp_id             
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def change_department (self , new_department):
        self.emp_department = new_department
        print("Employee new department is ",new_department)

    def print_employee_details (self):
        
        print("Name :",self.emp_name)
        print("ID :",self.emp_id)
        print("Salary :",self.emp_salary)
        print("Department :",self.emp_department)
    
    def calculate_emp_salary (self, emp_worktime):
        if emp_worktime > 50:
            overtime_hours = emp_worktime - 50
            overtime_amount = overtime_hours * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
            return total_salary
        else:
            total_salary = self.emp_salary
            return total_salary
    
Employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING") 
Employee2 = Employee("JONES","E7499", 45000, "RESEARCH") 
Employee3 = Employee("MARTIN","E7900", 50000, "SALES") 
Employee4 = Employee("SMITH","E7698", 55000, "OPERATIONS") 
Employee5 = Employee("SAM","E7545", 50000, "SALES")     

Employee1.print_employee_details()
Employee1.change_department("RESEARCH")
totalSalary = Employee1.calculate_emp_salary(60)
print(totalSalary)