import sqlite3


def colored_text(color, message):
    colors = {"red": "\033[31m", "blue": "\033[34m", "reset": "\033[0m"}
    return f"{colors[color]}{message}{colors['reset']}"



while True:
    print("\n1. הכנס רכב חדש לטיפול")
    print("2. סיום טיפול")
    print("3. הוצא רכב מהמוסך")
    print("4. בדיקת עומס טיפולים")
    print("5. יציאה")

    choice = input("בחר אופציה: ")
    conn = sqlite3.connect("databasehw.db")
    cur = conn.cursor()

    if choice == "1":
        car_number = input("הכנס מספר רישוי: ")
        car_problem = input("הכנס תיאור בעיה: ")
        owner_ph = input("הכנס מספר טלפון: ")
        try:
            cur.execute("INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES (?, ?, 0, ?)",
                        (car_number, car_problem, owner_ph))
            conn.commit()
            print(colored_text("blue", "הרכב נוסף בהצלחה!"))
        except sqlite3.IntegrityError:
            print(colored_text("red", "שגיאה: מספר הרכב כבר קיים במוסך."))

    elif choice == "2":
        car_number = input("הכנס מספר רישוי: ")
        cur.execute("SELECT fixed FROM garage WHERE car_number = ?", (car_number,))
        result = cur.fetchone()
        if not result:
            print(colored_text("red", "הרכב אינו במוסך."))
        elif result[0]:
            print(colored_text("red", "הטיפול כבר הסתיים."))
        else:
            cur.execute("UPDATE garage SET fixed = 1 WHERE car_number = ?", (car_number,))
            conn.commit()
            print(colored_text("blue", "הטיפול הסתיים בהצלחה!"))

    elif choice == "3":
        car_number = input("הכנס מספר רישוי: ")
        cur.execute("SELECT fixed, owner_ph FROM garage WHERE car_number = ?", (car_number,))
        result = cur.fetchone()
        if not result:
            print(colored_text("red", "הרכב אינו במוסך."))
        elif not result[0]:
            print(colored_text("red", "הטיפול עדיין לא הסתיים."))
        else:
            print(colored_text("blue", f"אנא התקשר לבעל הרכב: {result[1]}"))
            cur.execute("DELETE FROM garage WHERE car_number = ?", (car_number,))
            conn.commit()
            print(colored_text("blue", "הרכב הוצא מהמוסך!"))

    elif choice == "4":
        cur.execute("SELECT COUNT(*) FROM garage WHERE fixed = 0")
        count = cur.fetchone()[0]
        print(colored_text("blue", f"מספר רכבים ממתינים לתיקון: {count}"))

    elif choice == "5":
        conn.close()
        break

    else:
        print(colored_text("red", "בחירה לא תקפה."))

    conn.close()