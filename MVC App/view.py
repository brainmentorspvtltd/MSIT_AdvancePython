import controller
from getpass import getpass
import stdiomask


def loginSuccess(data):
    while True:
        print('''
            1. Post
            2. View Profile
            3. Update Profile
            4. Delete Profile
        ''')
        choice = input("Enter your choice: ")
        todo = {
            "1": post,
            "2": viewProfile,
            "3": updateProfile,
            "4": deleteProfile
        }
        (('ram', 'ram@gmail.com', 'ram1234'),)
        email = data[0][1]
        todo.get(choice)(email)


def post(email):
    pass


def viewProfile(email):
    pass


def updateProfile(email):
    pass


def deleteProfile(email):
    pass


def login():
    while True:
        email = input("Enter your email: ")
        if email.find('@') != -1:
            break
        print("Invalid email")
    password = stdiomask.getpass("Enter password:")
    result = controller.login(email, password)
    if isinstance(result, str):
        print(result)
        return
    loginSuccess(result)


def register():
    name = input("Enter your name: ")
    while True:
        email = input("Enter your email: ")
        if email.find('@') != -1:
            break
        print("Invalid email")
    # password = getpass("Enter password: ")
    password = stdiomask.getpass("Enter password: ", '#')
    # password = input("Enter your password: ")
    result = controller.register(name, email, password)
    print(result.__str__())


def main():
    print("""
        1. Login
        2. Register
    """)
    choice = input("Enter your choice: ")
    todo = {
        "1": login,
        "2": register
    }
    todo.get(choice)()


main()


'''
import sys
sys.path.append("..")
from controller import controller
'''

# CGI - Common Gateway Interface
