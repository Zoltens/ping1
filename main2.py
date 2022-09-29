import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='1111',
    host='127.0.0.1',
    port='5432',
    database='postgres_db'
)

cursor = connection.cursor()
cursor.execute("""CREATE TABLE posts (
    id INTEGER primary key, 
    author VARCHAR(50),
)""")
cursor.execute("""INSERT INTO users (id, author) VALUES (1, 'alex')""")
cursor.execute("SELECT admin FROM users WHERE username = '%s' % username)
cursor.execute("""SELECT author FROM posts WHERE author='alex'""")
connection.commmit()
cursor.close()
connection.close()
