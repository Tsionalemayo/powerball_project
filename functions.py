import random
from colorama import Fore,Style

todayNumbers = []

#מספרי הזכייה של היום

def todayNum():

    for i in range(5):
        x=(random.randint(1,20))
        while x in todayNumbers:
            x=(random.randint(1,20))
        todayNumbers.append(x)
        todayNumbers.sort()

    # הכדור ה-6 (Powerball)במספרי הזכיה
    powerball = random.randint(1, 10)
    todayNumbers.append(powerball)

    print("Today's Powerball Winning Numbers : ")
    print(Fore.BLUE,todayNumbers[0:5],Style.RESET_ALL,Fore.YELLOW,todayNumbers[-1],Style.RESET_ALL)

# ------------------------------------

luckyNumbers = []

#מספרי המזל
def luckyNum():

    for i in range(5):
        y=(random.randint(1, 20))
        while y in luckyNumbers:
            y = (random.randint(1, 20))
        luckyNumbers.append(y)
        luckyNumbers.sort()

#הכדור ה-6 (Powerball)במספרי המזל

    powerball = random.randint(1,10)
    luckyNumbers.append(powerball)

    print("Your's lucky Numbers : ")
    print(Fore.BLUE, luckyNumbers[0:5], Style.RESET_ALL, Fore.YELLOW, luckyNumbers[-1], Style.RESET_ALL)


# ---------------------------

# פונקציה שסופרת כמה כדורים לבנים קיימים בשני הרשימות
def countWhiteBalls():
    countWhite = 0
    for a in todayNumbers[0:5]:
        for b in luckyNumbers[0:5]:
            if a == b :
                countWhite+= 1

    return countWhite


#פונקציה שבודקת אם ה- powerball זהה בשני הרשימות
def countPowerBalls():
    countPower = 0

    if todayNumbers[-1] == luckyNumbers[-1]:
        countPower+=1

    return countPower


