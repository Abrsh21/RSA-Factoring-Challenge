"""This module contains helper functions for all the other modules used in this
    project
"""

def product(lst):
    """ Return product of all numbers in a list
    """
    prod = 1
    for _ in lst:
        prod *= _
    return prod

def gcd(p, q):
    """ Returns the greatest common divisor of the two numbers
    """
    while q:
        p, q = q, p % q
    return a

def kth_iroot(n, k):
    """ Return the integer k-th root of a number by Newton's method
    """
    u = n
    s = n + 1
    while u < s:
        s = u
        t = (k - 1) * s + n // pow(s, k - 1)
        u = t // k
    return s

def isqrt(n):
    """ Return the square root of a number rounded down to the closest integer
    """
    if n < 0:
        raise ValueError("Square root of negative number!")
    x = int(n)
    if n == 0:
        return 0
    p, q = divmod(x.bit_length(), 2)
    n = 2 ** (p + q)
    while True:
        y = (n + x // n) // 2
        if y >= x:
            return x
        x = y
