#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import model
import cgi
import base
print("Content-type:text/html\r\n\r\n")
# print("Inside profile controller")

form = cgi.FieldStorage()
contact = form.getvalue("contact")
dob = form.getvalue("dob")
occupation = form.getvalue("occupation")
interest = form.getvalue("interest")
# profilePic = form.getvalue("profilePic")
profilePic = form['profilePic']
email = form.getvalue("email")
oldProfilePic = form.getvalue("oldProfilePic")

base.startPage()
base.header(email)

# print(profilePic)
model.editProfile(contact, dob, occupation, interest,
                  profilePic, oldProfilePic, email)

base.footer()
