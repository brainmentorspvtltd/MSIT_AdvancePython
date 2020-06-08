class User:

    users = []

    def __init__(self):
        pass

    def menu(self):
        print("""
            1. Login
            2. Register
        """)
        choice = input("Enter your choice: ")
        todo = {
            "1": self.readUser,
            "2": self.createUser
        }
        print(todo)
        todo.get(choice)()

    def createUser(self):
        name = input("Enter your name: ")
        while True:
            email = input("Enter your email: ")
            if email.find('@') != -1:
                break
            print("Invalid email")

        password = input("Enter your password: ")
        user = {"name": name, "email": email, "password": password}
        self.users.append(user)
        print(user)
        print(self.users)

    def readUser(self):
        print("Read user")


user1 = User()
user1.menu()
user2 = User()
user2.menu()
