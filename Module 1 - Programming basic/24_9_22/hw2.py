'''
ערוך מדגם ממוצע גבהים של שחקני ה- NBA
צור רשימה ריקה
רוץ בלולאה וקלוט גבהי שחקנים ) float )בלולאה. אם הגובה שנקלט נמוך מ- 1.60 או
גבוה מ - 3.0 התעלם, רמז: continue. כל גובה תקין הוסף לרשימה באמצעות append
כאשר המשתמש יכניס גובה מינוס 999 צא מהלולאה
בתום הלולאה הדפס-
.1 כמה שחקנים נקלטו במדגם?
.2 מהו הגובה של השחק ן הכי גבוה?
.3 מהו הגובה של השחקן הכי נמוך?
.4 מהו ממוצע הגבהים של כל השחקנים?
.5 כמה שחקנים יותר גבוהים מ - 2.0 מטר?
.6 כמה שחקנים יותר גבוהים מהממוצע? )רמז: רוץ בלולאה על כל רשימת השחקנים ובדו ק
עבור כל גובה אם הוא גדול מהממוצע שחישבת קודם. אם כן הגדל את מונה הגבהים ב - 1(
'''


nba_list: list = []
players_count: int = 0
highest_player_height: float = 0.0
lowest_player_height: float = 999.0
sum_heights: float = 0.0
heigher_than_2_count: int = 0
players_heigher_than_avg: int = 0

while True:
    user_input: float = float(input("What is the height of the NBA player? "))
    if user_input == -999:
        print("Ok. Done.")
        break
    elif user_input < 1.60 or user_input > 3.0:
        #print("not good enough / not possible")
        continue
    else:
        #print("Appended.")
        players_count = players_count + 1
        nba_list.append(user_input)
        if lowest_player_height > user_input:
            lowest_player_height = user_input
        if highest_player_height < user_input:
            highest_player_height = user_input
        sum_heights = sum_heights + user_input
        if user_input > 2.0:
            heigher_than_2_count = heigher_than_2_count + 1

avg_heights = (sum_heights / players_count)
for x in nba_list:
    if x > avg_heights:
        players_heigher_than_avg = players_heigher_than_avg + 1
print(f"Players: {players_count}, Highest player: {highest_player_height}, Lowest player: {lowest_player_height},"
      f"Average heights: {avg_heights}, Heigher than 2: {heigher_than_2_count}, Players heigher than avg: {players_heigher_than_avg}")