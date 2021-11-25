
# vsota kvadratov prvih 100 števil

Stevila_do_100 = []
a = 1

while a<=100:
    Stevila_do_100.append(a)
    a = a + 1
print(Stevila_do_100)

KvadratiStevil = []
for i in Stevila_do_100: i**2 and KvadratiStevil.append(i**2)
print(KvadratiStevil)

VsotaKvadratov = sum(KvadratiStevil)
print(VsotaKvadratov)

# kvadrat vsote prvih 100 števil

Vsota_Stevila_do_100 = sum(Stevila_do_100)
Kvadrat_Vsota_sestevka = Vsota_Stevila_do_100**2
print(Kvadrat_Vsota_sestevka)

koncni_rezultat = Kvadrat_Vsota_sestevka - VsotaKvadratov
print(koncni_rezultat)