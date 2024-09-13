# *אתגר: יש בפאב 10 בירות . מותר להעניק בירה רק למי שמלאו לו 18 שנה. קלוט
# מהמשתמש את גילו. רק אם למשתמש מלאו 18 שנה הענק לו בירה. חזור על התהליך עד
# שחולקו כל 10 הבירות

beers_in_pub: int = 10 # beers

while True:
    if beers_in_pub == 0:
        print("No more beers!")
        break
    user_input: int = int(input("What is your age? "))
    if user_input > 120: print("Liar, liar pants on fire...\nbut,")  # just a joke :)
    if user_input >= 18:
        print("You get a beer!")
        beers_in_pub -= 1
        #print("Beers left in the pub: ", beers_in_pub)
    else:
        print("I'm sorry, you're underage.")