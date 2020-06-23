#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import cgi
import model
import home

form = cgi.FieldStorage()
email = form.getvalue("loginEmail")
password = form.getvalue("loginPassword")

result = model.login(email, password)
home.homePage(result)
