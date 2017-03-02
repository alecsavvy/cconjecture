#!/CConjecture/algorithm.py


def conjecture(n):
    """
    The Collatz Conjecture
    """          
    if isOdd(n):
        return odd(n)
    else:
        return even(n)


def isOdd(n):
    if n % 2 == 0:
        return False
    else:
        return True

def odd(n):
    n = (3*n)+1
    return n

def even(n):
    n = int(n/2)
    return n

