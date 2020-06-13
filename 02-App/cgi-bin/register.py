#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import cgi
form = cgi.FieldStorage()

name = form.getvalue("name")
email = form.getvalue("email")
password = form.getvalue("password")

print(f'''
<html>

<head>
    <title>Title</title>
</head>

<body>
    <h1>Regsiter Successful</h1>
    <h2>Name : {name}</h2>
    <h2>Email : {email}</h2>
</body>

</html>
''')
