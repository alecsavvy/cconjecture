"""

trying to prove each inbetween value resolves to a value in N.


3 - 10 - 5 - 16 --- 1
5 - 16 --- 1
6 - 3 --- 1
7 - 22 - 11 - 34 - 17 - 52 - 26 - 13 - 40 --- 10 --- 5 --- 1
9 - 28 - 14 - 7 --- 1
10 - 5 --- 1
11 --- 1
12 - 6 --- 1
13 --- 1
14 --- 1
15 - 46 - 23 - 70 - 35 - 106 - 53 - 160 --- 10 --- 5 --- 1


for odd numbers:
no iteration = O[ all odds ]
first iteration (3n + 1) = 01[in between 2nd comma (3, 5) = 4, move three commas to the right and subtract 1 from the next int in 0]
second iteration (n/2) = [first comma, next int after first pair, comma in between next two ints, next int after previous pair]

"""

N = []
in_between = []

oddnums = []
newodds = []
halfodds = []

def create():
    span = int(input("enter the span"))
    for num in range(0, span + 1):
        a1 = 4**num
        a2 = 2*a1
        N.append(a1)
        N.append(a2)

    for num in range(2, N[-1]):
        if num in N:
            continue
        else:
            in_between.append(num)

    N.remove(1)
    N.remove(N[-1])
    return None


def odds():
    span = int(input("enter the span"))
    n = 1
    for num in range(n, span, 2):
        oddnums.append(num)

    print(oddnums)

    for num in oddnums:
        num = (3*num) + 1
        newodds.append(num)

    for num in newodds:
        num = int(num/2)
        halfodds.append(num)

    print(newodds)
    print(halfodds)

    return None

odds()