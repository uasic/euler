# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


a = 999
b = 999
c = 0
ZbirkaPalindromov = []


while a>99:

        while b>99:
                zmnozek = a*b
                #print(zmnozek)
                #print(a)
                #print(b)
                res = str(zmnozek) == str(zmnozek)[::-1]
                if res == True:
                        ZbirkaPalindromov.append(zmnozek)
                        #print(ZbirkaPalindromov)
                        #print("Naslednji zmnozek je palindrom: ")
                        #print(zmnozek)
                        #print(a)
                        #print(b)
                        break
                else: 
                        #print("b se zniza")
                        b = b-1
                        
        #print("a se zniza")
        c=c+1
        a = a - 1
        #print("b je spet 999")
        b = 999 - c

max_value = max(ZbirkaPalindromov)
print(max_value)



        
    