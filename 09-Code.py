import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="root",
                             database="db_demo", autocommit=True)
cursor = connection.cursor()

name = "Ram"
email = "ram2@gmail.com"
password = "raman1212"
# query = f"insert into users values ('{name}', '{email}', '{password}')"
query = "insert into users values ( %s, %s, %s )"
# "insert into users values (Raman, raman@gmail.com, raman1212)"
# query = "insert into users values ( 'shyam', 'shyam@gmail.com', 'shyam1234' )"
# query = "select * from users"
cursor.execute(query, (name, email, password))
# data = cursor.fetchall()
# print(data)

connection.close()
