# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

stevilo = 600851475143
a = 2
zmnozek = 1

print("dela")

while zmnozek < stevilo:

    if stevilo%a == 0:
        #print("a je ")
        print(a)
        zmnozek = zmnozek * a  
        #print("zmnozek je ") 
        #print(zmnozek)
    a = a + 1
    
    