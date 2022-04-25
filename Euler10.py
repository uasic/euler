"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math
from math import sqrt


def je_prastevilo(num):
    if num < 2:
        return False # poglej funkcijo throw
    if num == 2:
        return True
    for n in range(2 , int(sqrt(num)) + 1):
        if num % n == 0:
            return False # stevilo ni prastevilo če je ta pogoj vsaj 1x res, return vedno zaključi funkcijo, takoj
    
    return True

a = 2
b = 2000000
vsota = 0
for a in range (2, b + 1):
    resitev = je_prastevilo(a)
    if resitev == True:
        vsota = vsota + a

print(vsota)