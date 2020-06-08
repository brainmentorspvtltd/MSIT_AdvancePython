def login():
    pass


def register():
    name = input("Enter your name: ")
    while True:
        email = input("Enter your email: ")
        if email.find('@') != -1:
            break
        print("Invalid email")

    password = input("Enter your password: ")


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
