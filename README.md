#THE COLLATZ CONJECTURE
A repository for my study of the Collatz Conjecture

The algorithm starts with any positive integer. If it is odd you multiply it by 3 and add 1. If it is even you divide by 2.
As you continuously iterate every integer will resolve to an endless loop of 4, 2, 1.
        
        pseudo-code example
        
        while n != 0:
            if n is odd:
                n = 3n+1
            if n is even:
                n = n/2
        
        >>> n = 1 
        >>> n = 3n+1
        >>> n = 4
        >>> n = n/2
        >>> n = 2
        >>> n = n/2
        >>> n = 1 
        
        back where we started, more info: https://en.wikipedia.org/wiki/Collatz_conjecture
        

No one has figured out why this works but I am curious so I will document my work in this repository.

There may be terms that I come up with over the course of this study so I will define them in the following file explanations below.

#algorithm.py
(created: 03/01/2017)
  
#main.py
(created: 03/01/2017)

#ph.py
(created: 03/01/2017)

#ch.py
(created: 03/01/2017)

- Savvy
