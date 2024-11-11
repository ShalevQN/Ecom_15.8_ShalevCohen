'''
כתוב תוכנית בפייטון הקולטת שמות של 4 שח קנים המשתתפים בהגרלה )str ),
עליך להגריל מתוך 4 השחקנים שחקן זוכה אחד באופן אקראי
הגרל מי השחקן שניצח והדפס את שמו. רמז: choice.random
'''
import random

players: list = [input("First player: "), input("Second player: "), input("Third player: "), input("Fourth player: ")]

#print(f"All the players are... {players}")
print(f"The winner is... {random.choice(players)}")