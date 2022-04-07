from prints import *

class Messages(Lottety):

    def __init__(self,name):
        super().__init__(name)

#פונקציה שמציגה למשתמש כמה כסף יקבל על סמך ההשוואה בין שתי רשימות המספרים

    def calMoney(self):
        w = super().countWhiteBalls()
        p = super().countPowerBalls()

        if w == 5:
            if p == 1:
                print(w, a)
            else:
                print(w, b)

        elif w == 4:
            if p == 1:
                print(w, c)
            else:
                print(w, d)

        elif w == 3:
            if p == 1:
                print(w, e)
            else:
                print(w, f)

        elif w == 2:
            if p == 1:
                print(w, g)
            else:
                print(h)

        elif w == 1:
            if p == 1:
                print(w, i)
            else:
                print(h)

        elif w == 0:
            if p == 1:
                print(j)
        else:
            print(h)
