"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed four million.

Regular recursive definition of Fibonacci quickly runs out of time or space for large values of n:
"""

def fib
 (n):
    if n is 1:
        return 1
    elif n is 2:
        return 2
    else:
        return fib(n-2)+fib(n-1)
 
#i.e., for a large n --
#RuntimeError: maximum recursion depth exceeded

#Trick - Use a lookup table to store the previously computed values:

table = {1:1, 2:2}
def fib(n):
    if n not in table:
        table[n] = fib(n-2)+fib(n-1)
    return table[n]

#This still doesn't work too well for very large values of n, but works very well for this problem.

def fib4m():
    n = 1
    total = 0
    val = fib(n)
    while (val < 4000000):
        if val % 2 == 0:
            total += val
        n += 1
        val = fib(n)
    return total