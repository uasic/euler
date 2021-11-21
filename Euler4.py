# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# najprej najdi največje 6 mestno število, ki je palindroms

# največje število, ki bi lahko bil zmnožek tromestnih števil je 999999

a = 9
b = 9

while a>0:

        while b>0:
                zmnozek = a*b
                print(zmnozek)
                res = str(zmnozek) == str(zmnozek)[::-1]
                if str(res) == True:
                        print("Naslednji zmnozek je palindrom: " + zmnozek)
                        exit()
                else: 
                        #print("b se zniza")
                        b = b-1
                        
        #print("a se zniza")
        a = a - 1
        #print("b je spet 999")
        b = 99

                


        
    