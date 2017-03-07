# !/CConjecture/trends.py

# ================================================================
"""

Collatz Conjecture, trends.py

This file displays the different trends that exist in the Collatz
Conjecture.

Trend 1: Powers of Four

    The root row has a relation to the powers of the integer 4.
    The root row is made up of every node that reduces to 1 strictly by n/2.
    let root_row = R = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, ..., infinity]

    We can also write R in this way:
        R = [a0, b0, a1, b1, a2, b2, ..., an, bn]
        where:
            a0 = 4^0 = 1;
            b0 = 2(a0) = 2;
            when n > 0:
                an = 2(bn-1), as in the b value in front of an, NOT b(n-1)
                bn = 2(an)

    Deduction:
        Every a value is directly related to a power of four:
            an = 4^n;
        Furthermore, every directly associated b value (such as an -> bn):
            bn = 2(an) = 2(4^n);
        This shows that every value in the root row is directly related to the powers of four.

    Notes:
        There is a trend in the parental hierachy for the root row that also coincides with the
        powers of four. Every a value is binary whereas the b values are not. This creates a
        noticable pattern in the root row matrix.

        example:

        4^0     2(4^0)  4^1     2(4^1)  4^2     2(4^2)  4^3     2(4^3)  4^4     2(4^4)  4^5     2(4^5)  4^6

        1-------2-------4-------8-------16------32------64------128-----256-----512-----1024----2048----4096
        |               |               |               |               |               |               |
        |               |               |               |               |               |               1365
        |               |               |               |               |               341-----682-----1364
        |               |               |               |               |                       |
        |               |               |               |               |                       227-----454
        |               |               |               |               |                               |
        |               |               |               |               |                               151
        |               |               |               |               |                               |
        |               |               |               |               |                               50
        |               |               |               |               85------170-----340-----680-----1360
        |               |               |               |                               |               |
        |               |               |               |                               |               453
        |               |               |               |                               113-----226-----452
        |               |               |               |                                       |
        |               |               |               |                                       75------150
        |               |               |               21------42------84------168-----336-----672-----1344
        |               |               5-------10------20------40------80------160-----320-----640-----1280
        |               |                       |               |               |               |
        |               |                       |               |               |               213-----426
        |               |                       |               |               53------106-----212-----424
        |               |                       |               |                       |
        |               |                       |               |                       35------70------140
        |               |                       |               13------26------52------104-----208-----416
        |               |                       |               |               |               |
        |               |                       |               |               |               3-------6
        |               |                       |               |               17------34------68------136
        |               |                       |               |                       |               |
        |               |                       |               |                       |               45
        |               |                       |               |                       11------22------44
        |               |                       |               |                               |
        |               |                       |               |                               7-------14
        |               |                       |               |                               |
        |               |                       |               |                               2-------4
        |               |                       |               |                                       |
        |               |                       |               |                                       1
        |               |                       |               1-------2-------4-------8-------16------32
        |               |                       |               |               |               |
        |               |                       |               0               |               5-------10
        |               |                       |                               |                       |
        |               |                       |                               |                       3
        |               |                       |                               1-------2-------4-------8
        |               |                       |                               |               |
        |               |                       |                               0               1-------2
        |               |                       |                                               |
        |               |                       |                                               0
        |               |                       |
        |               |                       |
        |               |                       3-------6-------12------24------48------96------192-----384
        |               1-------2-------4-------8-------16------32------64------128-----256-----512-----1024
        |               |               |               |               |               |               |
        |               |               |              \-------------------------------------------------/
        |               |               |
        |               |               1-------2-------4-------8-------16------32------64------128-----256
        |               |               |               |               |               |               |
        |               |               |               |              \---------------------------------/
        |               |               |               |
        |               |               |               1-------2-------4-------8-------16------32------64
        |               |               |               |               |               |               |
        |               |               |               |               |              \-----------------/
        |               |               |               |               |
        |               |               |               |               1-------2-------4-------8-------16
        |               |               |               |               |               |              \-/
        |               |               |               |               |               |
        |               |               |               |               |               1-------2-------4
        |               |               |               |               |               |               |
        |               |               |               |               |               |               1
        |               |               |               |               |               |               |
        0               0               0               0               0               0               0

        |-------------------------------------------------------------------------------------------------|


Trend 2: Static Rows

    If a row starts with a value that is divisible by 3 then the row is classified as static. This means that it does
    not generate any lower parents and only results from divisions of 2 until the algorithm hits 3.

    Well you would think that as that row approaches infinity there must be some number that would generate
    a lower parent, right? No.

    Take this row for example:
        R = [3, 6, 12, 24, ..., infinity] where each Rn = 2(Rn-1)
        (Pulled from the earlier example. This is a naturally occuring row.)

        By definition, for any of these values to have a lower parent they would need
            Rn = 3(k)+1 when k is an integer greater than 0 and Rn exists in R. k would then be the lower parent.

        Another required definition is what it takes to be a multiple of 3.
            An integer that is a multiple of 3 requires that the integer can be written strictly as a
            summation of 3s, with no remainder.
            example:
            6 = 3 + 3
            9 = 3 + 3 + 3
            ...
            y = 3 + 3 + 3 + ... + 3 , when y is a multiple of 3.

        In R our first value, R1, is 3, which is clearly its own multiple. The following values in the set
            are all determined by this multiple.
            R1 = 3, Rn+1 = 2(Rn).
            so R2 = 2(R1) = 6 = 3 + 3, therefore R2 and the rest of the data set have 3 as a multiple.

        Why does this quality inhibit any lower parents?
            We will take R2 as an example:
            R2 = 6 = 3 + 3

            upperParent(R2): 6*2 = 12
                = 3 + 3 + 3 + 3

            lowerParent(R2): 6 = 3(k) + 1, when k is an integer > 0.
                6 - 1 = 3(k)
                5 = 3(k)
                5/3 = k
                reason 1:
                    5 is not a multiple of 3.
                        5 = 3 + 2.
                reason 2:
                    5/3 is not an integer because the definition of an integer is any whole number,
                        and its negative counterpart.

        Conclusion:
            Any row that begins with an integer that has 3 as a multiple will not have any lower parents
            because subtracting 1 will terminate 3 as a multiple.


"""
# ================================================================