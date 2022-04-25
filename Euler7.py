"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

"""
test = 7
resitev = je_prastevilo(test)
if  resitev == False:
    print("stevilo ni prastevilo")
else:
    print("stevilo je prastevilo")

quit()
"""

limit = 1000000

a = 2
seznam_stevil = []

while a <= limit:
    seznam_stevil.append(a)
    a = a + 1
#print("Seznam vseh stevil:")
#print(seznam_stevil)


seznam_prastevil = []
for i in seznam_stevil:
    resitev = je_prastevilo(i)
    if resitev == True:
        seznam_prastevil.append(i)
        #print(seznam_prastevil)

#print("Seznam prastevil:")
#print(seznam_prastevil)


# poišči n-to praštevilo:

n_prastevilo = 10001
print (seznam_prastevil[n_prastevilo - 1])
# 104743 je rešitev







