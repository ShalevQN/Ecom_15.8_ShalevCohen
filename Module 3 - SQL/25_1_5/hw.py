import sqlite3
import os

db_name: str = "hw_solution.db"
if os.path.exists(db_name): # bonus
    os.remove(db_name)
else:
    print("File does not exist")
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


cursor.execute("CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);")

values_to_insert: list = [(1, 'Avokado', 5), (2, 'Milk', 2), (3, 'Bread', 3), (4, 'Chocolate', 8), (5, 'Bamba', 5), (6, 'Orange', 10)]

for value in values_to_insert: # kind of comprehended to save lines of code
    cursor.execute('''INSERT INTO shopping VALUES (?, ?, ?)''', value)

conn.commit()

print("Select all:")

cursor.execute("SELECT * FROM shopping")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

print("where amount > 5:")

cursor.execute("SELECT * FROM shopping WHERE amount > 5")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

cursor.execute("DELETE from shopping WHERE name like 'Orange'")

cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")

cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")

conn.commit() # not sure if its necessary but it works without it. lmk :)

# print("Select all after changes:")
# cursor.execute("SELECT * FROM shopping")
# rows = cursor.fetchall()
# for row in rows:
#     print(tuple(row))

print("count(*):")

cursor.execute("SELECT COUNT(*) from shopping")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

print("select all where id > 0:")

cursor.execute("SELECT * FROM shopping WHERE id > 0")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

conn.close()