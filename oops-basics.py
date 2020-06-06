Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Emp:
	id = 101
	name = "Ram"
	age = 45
	salary = 45000

	
>>> Emp
<class '__main__.Emp'>
>>> # class name should always start with a capital letter
>>> Emp()
<__main__.Emp object at 0x10f2edda0>
>>> emp = Emp()
>>> emp
<__main__.Emp object at 0x111238be0>
>>> emp.age
45
>>> emp.name
'Ram'
>>> emp.name = "Raman"
>>> emp.name
'Raman'
>>> emp.__dict__
{'name': 'Raman'}
>>> emp.dept = "IT"
>>> emp.dept
'IT'
>>> emp.__dict__
{'name': 'Raman', 'dept': 'IT'}
>>> 
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Emp:
	id = 101
	name = "Ram"
	age = 45
	salary = 45000

	
>>> emp = Emp()
>>> emp.id
101
>>> emp.name
'Ram'
>>> emp.name = "Raman"
>>> emp.dept = "IT"
>>> emp.__dict__
{'name': 'Raman', 'dept': 'IT'}
>>> 
>>> emp1 = Emp()
>>> emp2 = Emp()
>>> emp1.id
101
>>> emp2.id
101
>>> emp1.name
'Ram'
>>> emp2.name
'Ram'
>>> 
>>> class Emp:
	id = None
	name = None
	age = None
	salary = None

	
>>> emp1 = Emp()
>>> emp2 = Emp()
>>> emp1.id
>>> emp2.id
>>> emp1.id = 101
>>> emp1.name = "Ram"
>>> emp1.name = 45
>>> emp1.salary = 45000
>>> emp1.__dict__
{'id': 101, 'name': 45, 'salary': 45000}
>>> emp1.age = 45
>>> emp1.name = "Ram"
>>> emp1.__dict__
{'id': 101, 'name': 'Ram', 'salary': 45000, 'age': 45}
>>> #  __dict__ property of an object tells us which member variables(variables inside an object) you have assigned values to
>>> type(12)
<class 'int'>
>>> isinstance(12,int)
True
>>> isinstance( emp1 , Emp)
True
>>> emp2.id = 102
>>> emp2.name = "Shyam"
>>> emp2.age = 29
>>> emp2.salary = 35000
>>> emp2.__dict__
{'id': 102, 'name': 'Shyam', 'age': 29, 'salary': 35000}
>>> emp2.__dir__()
['id', 'name', 'age', 'salary', '__module__', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> 
