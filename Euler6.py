# 2050 je najmanjse stevilo, ki ga lahko delijo vsa stevila od 1 do 10 brez 
# ostanka. Katero je najmanjse stevilo,ki ga tako delijo vsa stevila od 1 do 20?

a = 20
d = 1

while 1>0:
    while a%d == 0:
        d = d + 1
        if d == 20:
            print(a)
            quit()
    a = a + 20
    d = 1