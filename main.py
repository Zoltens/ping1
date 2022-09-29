import psycopg2


connection = psycopg2.connect(
    user='postgres',
    password='1111',
    host='127.0.0.1',
    port='5432',
    database='postgres_db'
)

cursor = connection.cursor()
cursor.execute("""CREATE TABLE users (
    id INTEGER primary key, 
    name VARCHAR(50),
    type VARCHAR(50)
)""")
cursor.execute("""INSERT INTO users (id, name) VALUES (1, 'alex', 'admin')""")
cursor.execute("""INSERT INTO user (id, name) VALUES  (2, 'andre', 'stuff')""")
cursor.execute("""SELECT type FROM users WHERE type='+type+'""")
connection.commmit()
cursor.close()
connection.close()


