values_to_insert: list = [(1, 'Avokado', 5), (2, 'Milk', 2), (3, 'Bread', 3), (4, 'Chocolate', 8), (5, 'Bamba', 5), (6, 'Orange', 10)]

for value in values_to_insert:
    cursor.execute('''INSERT INTO shopping VALUES (?, ?, ?)''', value)