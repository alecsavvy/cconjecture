#!/CConjecture/ph.py
from datetime import date


class Tree:
    def __init__(self, rounds):
        self.date = date.today()
        self.id = tuple(self.date)
        self.rounds = rounds
        self.row = []
        self.rows = 0
        self.grid = {}

    def getid(self):
        return self.id

    def getRounds(self):
        return self.rounds

    def getRows(self):
        return self.rows


class Node:
    def __init__(self, num, row, parent1, parent2=False):
        self.num = num
        self.parent1 = parent1
        self.row = row
        if parent2:
            self.parent2 = parent2
        else:
            self.parent2 = False

    def getNum(self):
        return self.num

    def getParentOne(self):
        return self.parent1

    def getParentTwo(self):
        if self.parent2:
            return self.parent2
        else:
            return "0"

    def getRow(self):
        return self.row


def main(rounds):
    while rounds != 0:
        counter = 0
        n = 1
        rowName = "row" + str(n)


    return None


def lowerGen(num):
    newnum = num - 1
    if newnum % 3 != 0:
        return False
    else:
        return True


def higherGen(num):
    return num * 2


def run():
    print(date.today())
    print("there will be a parental simulation here")
    main()
    return None

run()
