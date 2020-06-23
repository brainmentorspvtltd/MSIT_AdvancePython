#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import cgi
import model
import home

form = cgi.FieldStorage()
name = form.getvalue("registrationName")
email = form.getvalue("registrationEmail")
password = form.getvalue("registrationPassword")
city = form.getvalue("registrationCity")
gender = form.getvalue("gender")

result = model.register(name, email, password, city, gender)
home.homePage(result)
