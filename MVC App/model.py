import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="root",
                             database="db_demo", autocommit=True)
cursor = connection.cursor()


class User:

    # users = []

    # parameterised constructor (cons with parameters other than self)
    def __init__(self, name, email, password):
        self.__name = name
        self.email = email
        self.password = password

    # This fn will be called automatically whenever we try to print the Object
    # this fn returns a string representation of object details that are shown to the user instead of the memory location thing
    def __str__(self):
        return f"{self.name},{self.email},{self.password}"
        # return f"Name is {self.name}, email is {self.email}, password is {self.password}"

    # def storeDetails(self):
    #     User.users.append([self.name, self.email, self.password])

    # def showDetails(self):
    #     pass


# users = []


def login(email, password):
    query = "select * from users where email = %s and password = %s"
    cursor.execute(query, (email, password))
    # cursor.rowcount()
    data = cursor.fetchall()
    if len(data) < 1:
        return "User doesn't exist..."
    else:
        return data


def register(name, email, password):
    user = User(name, email, password)
    # users.append(user)
    query = "insert into users values (%s, %s, %s)"
    try:
        cursor.execute(query, (name, email, password))
        return user
    except pymysql.err.IntegrityError:
        return "Email ID already exists..."
    # print(user.__str__())
    # for key in dict1.keys():
    #     print(key)
    # print("Hello world", end='\n')
    # user.storeDetails()
    # print(User.users)


'''
Sql - Structured Query Language

1. Download and install mysql
2. Goto bin folder
3. Open cmd inside bin and type ‘mysqld’ daemon and hit enter => it will start mysql server
4. Open another cmd and type ‘mysql -u root -p’ and hit enter

Alternative 
1. Download and install xampp
'''

user = User("Ram", "ram@gmail.com", "ram1234")
user.__name = "Abc"
print(user.__name)
