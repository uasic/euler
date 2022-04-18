"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt
import math
import sys

"""
def preveri(x):
    y = int(x)
    print(x == y)

preveri(3.33)
preveri(3.00)
#exit
"""

a=1
b=1
c2 = a*a + b*b
c = sqrt(c2)
vsota = 0
#print(c)

while b < 1000:

    while a < 1000:

        c2 = a*a + b*b # to je c na kvadrat
        #print(c2)
        c_sqrt = sqrt(c2)
        #print(c_sqrt)
        c_int = int(c_sqrt)
        #print(c_int)

        if c_sqrt == c_int:

            c = c_int
            vsota = a + b + c

            if vsota > 1000:
                break

            #print(a , b , c , vsota)

            if vsota == 1000:
                print(a)
                print(b)
                print(c)
                print("zmnozek abc:")
                print(a*b*c)
                quit()

        a = a + 1
        #print(a)

    a = 1
    b = b + 1
    #print(b)

    
