#!/cconjecture/ex.py
import algorithm as a

def getInput():
    num = input("what number do you want to test?")
    while True:
        try:
            num = int(num)
            if num > 0:
                return num
            else:
                print("please enter an integer greater than 0")
                continue
        except ValueError:
            print("please enter an integer")
            continue


def run():
    n = getInput()
    print("starting value: ")
    print(n)
    while n != 1:
        n = a.conjecture(n)
        print(n)

    ex = input("would you like to test another number?")
    if ex == "no":
        return None
    else:
        run()

run()
