import pymysql
connection = pymysql.connect(host="localhost", port=3306, user="root",
                             database="db_demo", autocommit=True)
cursor = connection.cursor()

query = "insert into users values ( 'shyam', 'shyam@gmail.com', 'shyam1234' )"
cursor.execute(query)

connection.close()
