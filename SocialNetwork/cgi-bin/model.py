import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="root",
                             database="socialnetwork", autocommit=True)
cursor = connection.cursor()


class User:
    def __init__(self, name, email, password, city, gender):
        self.__name = name
        self.email = email
        self.password = password
        self.city = city
        self.gender = gender

    def __str__(self):
        return f"{self.name},{self.email},{self.password},{self.city},{self.gender}"


def login(email, password):
    query = "select * from users where email = %s and password = %s"
    cursor.execute(query, (email, password))
    # cursor.rowcount()
    data = cursor.fetchone()
    if data == None:
        return "User doesn't exist..."
    else:
        return data


def register(name, email, password, city, gender):
    user = User(name, email, password, city, gender)
    # users.append(user)
    query = "insert into users values (%s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, (name, email, password, city, gender))
        return "Registration Successful..."
    except pymysql.err.IntegrityError:
        return "Email ID already exists..."


# print(login("anmol@gmail.com", "anmol123"))