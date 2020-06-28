import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="root",
                             database="socialnetwork", autocommit=True)
cursor = connection.cursor()


class User:
    def __init__(self, name, email, password, city, gender):
        self.name = name
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
        return user
    except pymysql.err.IntegrityError:
        return "Email ID already exists..."


def editProfile(contact, dob, occupation, interest, profilePic, oldProfilePic, email):
    cursor.execute("delete from profile where email = %s", (email))
    query = "insert into profile values (%s, %s, %s, %s, %s, %s)"
    if email == "None":
        raise pymysql.IntegrityError("Email address cant be none")
    if profilePic.filename:
        open("profile_pic/" + profilePic.filename,
             'wb').write(profilePic.file.read())
        cursor.execute(query, (contact, dob, occupation,
                               interest, profilePic.filename, email))
    else:
        cursor.execute(query, (contact, dob, occupation,
                               interest, oldProfilePic, email))


def fetchProfile(email):
    query = "select * from profile where email = %s"
    cursor.execute(query, (email))
    data = cursor.fetchone()
    if data is None:
        return ('', '', '', '', '', '')
    return data


# print(login("anmol@gmail.com", "anmol123"))

#     print(f"<h3>Profile picture is {profilePic}</h3>")
    # fileStream = open("profile_pic/" + profilePic.filename, 'wb')
    # fileStream.write(profilePic.file.read())
    # print(f"type is {type(profilePic.file)}")
    # print(profilePic.file.read())
