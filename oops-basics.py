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
