class Employee:
    # Initializing the constructor
    emp_count = 0
    emp_salaries = 0

    def __init__(self, name, family, salary, department):
        self.emp_department_name = department
        self.emp_salary = salary
        self.emp_family = family
        Employee.emp_count += 1
        Employee.emp_salaries = Employee.emp_salaries + self.emp_salary
        self.emp_name = name

    def get_salary(self):
        total_salaries = 0
        total_salaries = Employee.emp_salaries/Employee.emp_count
        return total_salaries

    # Inheriting the Employee class to FullTimeEmployee Class


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


f1 = FullTimeEmployee("sahaja", "Adavelli", 1800000, "CS")
f2 = FullTimeEmployee("Sree", "tata", 1200000, "CSE")
f3 = FullTimeEmployee("valli", "x", 600000, "CS")
avg_salary = f2.get_salary()
print("All the employees together has an average salary of", avg_salary)


