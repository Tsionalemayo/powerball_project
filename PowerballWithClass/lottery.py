import random
from colorama import Fore,Style
from powerball_project.PowerballWithClass.game import Game

class Lottety(Game):
    todayNumbers = []
    luckyNumbers = []
    def __init__(self,name):
        super().__init__(name)

    # מספרי הזכייה
    # todayNumbers = []
    def todayNum(self):
        for i in range(5):
            x = (random.randint(1, 20))
            while x in self.todayNumbers:
                x = (random.randint(1, 20))
            self.todayNumbers.append(x)
            self.todayNumbers.sort()

        # הכדור ה-6 (Powerball)במספרי הזכיה
        powerball = random.randint(1, 10)
        self.todayNumbers.append(powerball)

        print("Today's Powerball Winning Numbers : ")
        print(Fore.BLUE,self.todayNumbers[0:5],Style.RESET_ALL,Fore.YELLOW,self.todayNumbers[-1],Style.RESET_ALL)
        return self.todayNumbers

    # todayNum()

    # ------------------------------------
    # luckyNumbers = []
    # מספרי המזל
    def luckyNum(self):
        for i in range(5):
            y = (random.randint(1, 20))
            while y in self.luckyNumbers:
                y = (random.randint(1, 20))
            self.luckyNumbers.append(y)
            self.luckyNumbers.sort()

        # הכדור ה-6 (Powerball)במספרי המזל

        powerball = random.randint(1, 10)
        self.luckyNumbers.append(powerball)

        print("Your's lucky Numbers : ")
        print(Fore.BLUE,self.luckyNumbers[0:5],Style.RESET_ALL,Fore.YELLOW,self.luckyNumbers[-1],Style.RESET_ALL)
        return self.luckyNumbers


    # פונקציה שסופרת את מספר הכדורים הלבנים שנמצאים בשני הרשימות
    def countWhiteBalls(self):
        self.run()
        countWhite = 0
        for a in self.todayNumbers[0:5]:
            for b in self.luckyNumbers[0:5]:
                if a == b:
                    countWhite += 1

        # print(countWhite)

        return countWhite

    #   פונקציה שבודקת אם יש powerball בשני הרשימות
    def countPowerBalls(self):
        countPower = 0
        if self.todayNumbers[-1] == self.luckyNumbers[-1]:
            countPower += 1

        # print(countPower)

        return countPower


    def run(self):
        self.todayNum()
        self.luckyNum()