class Employee:
    # constructor # magic method
    # this fn will be automatically called when we create Employee object
    def __init__(self):
        print("Constructor called")
        self.id = None
        self.name = None
        self.salary = None
        self.age = None
        self.company = "ABC Pvt. Ltd."
        self.employeeDetails = []   # unique list for an object

    def showDetails(self):
        print("Employee1 id is", self.id)
        print("Employee1 name is", self.name)
        print("Employee1 salary is", self.salary)
        print("Employee1 age is", self.age)
        print("Employee1 company is", self.company)

    def setEmployeeDetails(self):
        self.employeeDetails.append(
            [self.id, self.name, self.salary, self.age, self.company])


employee1 = Employee()
employee1.id = 101
employee1.name = "John"
employee1.salary = 45000
employee1.age = 40
employee1.setEmployeeDetails()
print(employee1.employeeDetails)


employee2 = Employee()
employee2.id = 102
employee2.name = "Jenny"
employee2.salary = 40000
employee2.age = 35
employee2.company = "XYZ, Inc."
employee2.setEmployeeDetails()
print(employee2.employeeDetails)

employee3 = Employee()
employee3.id = 103
employee3.name = "Ram"
employee3.salary = 20000
employee3.age = 25
employee3.company = "XYZ, Inc."
employee3.setEmployeeDetails()
print(employee3.employeeDetails)
