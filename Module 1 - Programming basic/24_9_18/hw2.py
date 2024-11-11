'''
בקפיצה לגובה עם מוט )פול וולט( באולימפיאדה, שיא העולם הנוכחי לגברים עומד
על 6.23 מטרים ,והוא נקבע על ידי ארמנד דופלנטיס (Duplantis Armand (בשנת 2023 .
תוצאה של מעל 5.80 מטרים נחשבת טובה מאוד בתחרויות ברמה האולימפית, כאשר הזוכים
לרוב קופצים מעל 6.00 מטרים.
כתוב תוכנית בפייטון הקולטת תוצאות קפיצה לגובה של 7 מדינות באולימפיאדה .
אם הגיעה תוצאה מתחת ל - 5.80 התעלם. רמז: continue
אם הגיעה תוצאה טובה של 5.80 ומעלה ספור אותה
אם אחת הקפיצות שברה את שיא העולם, קלוט את שם הספורטאי שהשיג את התוצאה
'''

best_score: float = 0
good_scores_count: int = 0
world_record_player = None
scores_sum: float = 0
world_record_score: float = 0

for x in range(7):
    user_input: float = float(input("What is the height that the player reached? "))
    if user_input >= 5.8:
        if user_input > best_score:
            best_score = user_input
        good_scores_count += 1
        scores_sum += user_input
        if user_input > 6.23:
            world_record_score = user_input
            world_record_player = input("He broke a world record! What the player's name? ")
    else:
        continue

avg_scores: float = scores_sum / 7
print(f"There were {good_scores_count} good scores and the average for them were: {avg_scores} (best score was {best_score}).")
if world_record_player is not None:
    print(f"Theres a new world record! The record is {world_record_score} by {world_record_player}")
else:
    print(None)