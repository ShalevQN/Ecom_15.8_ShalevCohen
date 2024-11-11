'''
עליך לחשב ממוצע טמפרטורה של 5 ערים בעולם
רוץ בלולאה מ- 1 עד 5 ובכל פעם קלוט את הטמפרטורה
אם הטמפרטורה קטנה ממינוס 50 או גדולה מפלוס 45 קלוט שוב ושוב, עד אשר הטמפרטורה
תהיה בטווח.
בתום הקלט של 5 הערים , חשב את ממוצע הטמפרטורה. רמז: ראה קוד של השיעור
'''

temp_cities: int = 0

for x in range(5):
    while True:
        temp: int = int(input("What is your city temperature?"))
        if -50 < temp < 45:
            temp_cities += temp
            break
        else:
            print("Not in range...")
avg_temps = temp_cities / 5
print(avg_temps)


# temp_cities: list = []
# for x in range(5):
#     while True:
#         temp: int = int(input("What is your city temperature?"))
#         if -50 < temp < 45:
#             temp_cities.append(temp)
#             break
#         else:
#             print("Not in range...")
# avg_temps = sum(temp_cities) / len(temp_cities)
# print(int(avg_temps))