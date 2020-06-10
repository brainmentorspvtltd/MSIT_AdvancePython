import controller
from getpass import getpass
import stdiomask


def login():
    pass


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
