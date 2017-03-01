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
    return 3n+1

def even(n):
    return n/2

