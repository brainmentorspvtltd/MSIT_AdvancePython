import turtle


class Employee:
    '''This is Employee class'''
    id = None   # property
    name = None    # member variable
    salary = None
    age = None
    company = "ABC Pvt. Ltd."

    # self -> current object (this)
    # self holds the referecne of function owner
    # self = employee1 or self = employee2
    # current object the object that has called this function currently
    # whenever you create an object inside class, the first argument is always going to be 'self'
    def showDetails(self):  # member function (methods)
        '''Prints details of a particular employee'''
        print("Employee1 id is", self.id)
        print("Employee1 name is", self.name)
        print("Employee1 salary is", self.salary)
        print("Employee1 age is", self.age)
        print("Employee1 company is", self.company)


employee1 = Employee()
employee1.id = 101
employee1.name = "John"
employee1.salary = 45000
employee1.age = 40
print(employee1.__dir__())
print("employee1 is of type", employee1.__class__)
print("employee1 is of type", employee1.__class__.__name__)
print(employee1.__doc__)
print(turtle.__doc__)
print(employee1.showDetails.__doc__)
print(turtle.readconfig.__doc__)
print(str.endswith.__doc__)

employee1.showDetails()

print(employee1.__dict__)
print(isinstance(employee1, Employee))

employee2 = Employee()
employee2.id = 102
employee2.name = "Jenny"
employee2.salary = 40000
employee2.age = 35
employee2.company = "XYZ, Inc."
print(employee2.__dict__)

employee2.showDetails()
