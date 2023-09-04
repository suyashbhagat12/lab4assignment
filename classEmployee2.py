class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

def sort_employees(employees, key):
    if key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return employees

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Select a sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        choice = int(input("Enter your choice: "))
        sorted_employees = sort_employees(employees, choice)
        
        print("Sorted Employee Data:")
        for emp in sorted_employees:
            print(emp)
    except ValueError:
        print("Invalid input. Please enter a number.")

if _name_ == "_main_":
    main()