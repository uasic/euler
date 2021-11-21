# If we list all the natural numbers below 10 
#that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

i = 3
j = 5
vsota_i = 0
vsota_j = 0
vsota = 0

while i < 1000:
    vsota_i = vsota_i + i
    i = i + 3

while j < 1000:
    if j%3 != 0:
        vsota_j = vsota_j + j
        j = j + 5
    else: 
        j = j + 5

vsota = vsota_i + vsota_j
print(vsota)
