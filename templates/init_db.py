import sqlite3

with open('schema.sql') as sql_file:
	sql_script = sql_file.read()

connection = sqlite3.connect('database.db')

cur = connection.cursor()
cur.executescript(sql_script)

cur.execute("INSERT INTO posts (title,content) VALUES (?,?)",
	("FIRST INTO posts", 'Content for the first post')
	)

cur.execute("INSERT INTO posts (title,content) VALUES (?,?)",
	("SECOND INTO posts", 'Content for the second post')
	)

connection.commit()
connection.close()