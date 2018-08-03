import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()   #similar to a screen cursor, it allows us to selct and start thinigs. It executes the queries

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


user = (1, "damien", "bitches")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
      (2, "not damien", "notbitches"),
      (3, "other", "otherps")
      ]
cursor.executemany(insert_query, users)

select_query = "SELECT * from users"
a = cursor.execute(select_query)
res = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    print (name[0])
print(next(a))

connection.commit()

connection.close()