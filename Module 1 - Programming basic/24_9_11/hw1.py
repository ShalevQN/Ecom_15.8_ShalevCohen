'''
כתוב תוכנית בפייטון הקולטת מהמשתמש אורך סרט בדקות ומדפיסה כמה שעות, וכמה דקות
נמשך הסרט . לדוגמא :
- אם אורך הסרט שנקלט הוא - ,70 אז התשובה תהיה 1 שעה ו- 10 דקות
- אם אורך הסרט שנקלט הוא - ,160 אז התשובה תהיה 2 שעות ו- 40 דקות
- אם אורך הסרט שנקלט הוא - ,180 אז התשובה תהיה 3 שעות ו- 0 דקות
- וכו'
'''

movie_minutes: int = int(input("Welcome to the movies,\nhow long of a move do you want to watch? (in minutes:) "))
print(f"The movie will be {movie_minutes // 60} hours and {movie_minutes % 60} minutes")