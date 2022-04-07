# from utilities import todayNum,luckyNum,countWhiteBalls,countPowerBalls
from functions import *

class Messages:

    def calMoney(w, p):
        w = countWhiteBalls()
        p = countPowerBalls()

        if w == 5:
            if p == 1:
                print(w, "Correct White Balls and the Powerball: Jackpot $324,000,000")
            else:
                print(w, "Correct White Balls, but no Powerball: $1,000,000 ")

        elif w == 4:
            if p == 1:
                print(w, "Correct White Balls and the Powerball: $10,000 ")
            else:
                print(w, "Correct White Balls, but no Powerball: $100")

        elif w == 3:
            if p == 1:
                print(w, "Correct White Balls and the Powerball: $100 ")
            else:
                print(w, "Correct White Balls, but no Powerball: $7")

        elif w == 2:
            if p == 1:
                print(w, "Correct White Balls and the Powerball: $7")
            else:
                print("Try again! ")

        elif w == 1:
            if p == 1:
                print(w, "Correct White Ball and the Powerball: $4")
            else:
                print("Try again !")

        elif w == 0:
            if p == 1:
                print("No White Balls, Just the Powerball: $4 ")
            else:
                print("Try again")
        else:
            print("Try again")

    calMoney(todayNum(),luckyNum())