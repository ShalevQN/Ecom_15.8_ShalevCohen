import sqlite3

# connector
db_name: str = "hwsql1.db"
conn = sqlite3.connect(db_name) # creates a connector
conn.row_factory = sqlite3.Row # allow me to use column name

# cursor
cursor = conn.cursor()  # creates a cursor

cursor.execute("SELECT * FROM grades")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

conn.close()
