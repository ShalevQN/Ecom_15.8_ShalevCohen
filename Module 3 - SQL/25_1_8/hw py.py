import sqlite3
import sqlitelib

db_name: str = "hwsql3.db"
conn, cursor = sqlitelib.connect_db(db_name)


result = sqlitelib.read_query(cursor, "SELECT topic FROM courses")
for item in result:
    print(item)


course_name = input('Enter new course name: ')
if course_name in [item[0] for item in result]: # bonus
    raise ValueError("Course name already exist.")
else:
    course_hours = float(input('How much hours will the course have? '))
    sqlitelib.update_query(
        cursor, conn,
        "INSERT INTO courses (topic, hours) VALUES (?, ?)",
        (course_name, course_hours))


print("Updated courses list:")
result = sqlitelib.read_query(cursor, "SELECT topic FROM courses")
for item in result:
    print(item)


conn.close()