#!/CConjecture/ph.py

class Num:
    def __init__(self, num, isElbow, parent1, parent2=False):
        self.num = num
        self.parent1 = parent1
        self.isElbow = isElbow
        if parent2:
            self.parent2 = parent2
        else:
            self.parent2 = None

    def __str__(self):
        return str(num)

    def getNum(self):
        return self.num

    def getParentOne(self):
        return self.parent1

    def getParentTwo(self):
        return self.parent2

    def getIsElbow(self):
        return self.isElbow


def genParentRow(n):
    row = {}
    parent1 = 0
    counter = 1
    for k in range(n):
        name = counter
        counter += 1
        
        num = 4**k
        num1 = Num(num,True,parent1)
        row[name] = num1

        name = counter
        counter += 1

        num = 2*num
        parent1 = num1.getNum()
        num2 = Num(num,False,parent1)
        row[name] = num2

        parent1 = num2.getNum()

    for entry in row:
        print()
        print(entry)
        print(row[entry].getNum())
    return None


def genMatrix():
    return None





def main():
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
    #print(date.today())
    print("there will be a parental simulation here")
    main()
    return None

run()
genParentRow(5)
