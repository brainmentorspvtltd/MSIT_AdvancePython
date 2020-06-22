import cgi
import model

form = cgi.FieldStorage()
name = form.getvalue("registrationName")
email = form.getvalue("registrationEmail")
password = form.getvalue("registrationPassword")
city = form.getvalue("registrationCity")
gender = form.getfield("gender")

model.register(name, email, password, city, gender)
