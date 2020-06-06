# emp = {
#     "id": 101,
#     "name": "John"
# }
# emp['id']
# list1[0]


class Employee:
    id = None   # property
    name = None    # member variable
    salary = None
    age = None
    company = "ABC Pvt. Ltd."

    # whenever you create an object inside class, the first argument is always going to be 'self'
    def showDetails(self):   # member function (methods)
        pass


employee1 = Employee()
employee1.id = 101
employee1.name = "John"
employee1.salary = 45000
employee1.age = 40
print(employee1.__dir__())

print("Employee1 id is", employee1.id)
print("Employee1 name is", employee1.name)
print("Employee1 salary is", employee1.salary)
print("Employee1 age is", employee1.age)
print("Employee1 company is", employee1.company)
print(employee1.__dict__)

print(type(employee1))
print(isinstance(employee1, Employee))
print(isinstance(employee1, str))
print(isinstance("employee1", str))
# print(dir(employee1))

employee2 = Employee()
employee2.id = 102
employee2.name = "Jenny"
employee2.salary = 40000
employee2.age = 35
employee2.company = "XYZ, Inc."

print("Employee2 id is", employee2.id)
print("Employee2 name is", employee2.name)
print("Employee2 salary is", employee2.salary)
print("Employee2 age is", employee2.age)
print("Employee2 company is", employee2.company)
print(employee2.__dict__)

# jobTitle.text
# emp.keys()
# list1.sort()


# html = bs4.BeautifulSoup()
# Pen()
# Screen()
# SysFont()
# BeautifulSoup()
