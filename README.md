#THE COLLATZ CONJECTURE

A repository for my study of the Collatz Conjecture

The algorithm starts with any positive integer. If it is odd you multiply it by 3 and add 1. If it is even you divide by 2.
As you continuously iterate every integer will resolve to an endless loop of 4, 2, 1.


#python3 code example

        def run(n):
            # n is an int > 0
            while n != 0: 
                # infinite because 0 is unreachable
                if n % 2 != 0:
                    # n is odd
                    n = 3n+1
                    print(n)
                else:
                    # n is even
                    n = n/2
                    print(n)
            return None
        
        
        >>> run(1)  # starting algorithm at 1
        >>> 4       # n = 3(1)+1
        >>> 2       # n = (4)/2
        >>> 1       # n = (2)/2 loop repeats
        >>> 4       # n = 3(1)+1
        >>> 2       # n = (4)/2
        >>> 1       # n = (2)/2 continues infinitely
        >>> quit() 
        
        

No one has figured out why this works but I am curious so I will document my work in this repository. If you want to test this yourself you can run ex.py.


There may be terms that I come up with over the course of this study so I will define them in the following file explanations below.

more info: https://en.wikipedia.org/wiki/Collatz_conjecture


#algorithm.py
(created: 03/01/2017)
  
  
#main.py
(created: 03/01/2017)

Initializes the entire project with a user interface through the console. As of right now this is built to run from terminal. You can run this from idle or any other IDE you're comfortable with.
        
        cd path/cconjecture
        savvy$ python3 main.py

#ph.py
(created: 03/01/2017)


Parent: a potential previous node from an integer

Parental Hierarchy: The accumulation of every potential parent node and following parents from a starting integer. For example, 2 has one parent which is 4. This is because 4/2 is 2. If we try to find the other parent for 2 [ 2 = 3n+1 ] we get 1/3 which is not an integer, and therefore not an option. 


#trends.py
(created: 03/06/2017)

Contains all of the proofs for the Collatz Conjecture, or at least the proofs of any trends I find.

#ex.py
(created: 03/01/2017)

Simple example program that asks for an integer if you want to watch the Collatz Conjecture in action.

-Savvy
