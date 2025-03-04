from time import *

#V5 Rühm 20 õpilast sooritas ühe sessiooni jooksul kolm eksamit. Tehke algoritm eksamivormi täitmiseks.

for student in range(20):
    print(f"Soritab eksamit {student+1}. õpilane")
    for exam in range(3):
        print(f"{exam+1}. eksam")

#V4 Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.

#vastus = 0
#p=int(input("Mitu korda kordame?"))
#while True:
 #   arv = float(input("Sisesta arv: "))
  #  if arv < 0:
   #     vastus += arv
    #p -= 1
    #if p == 0:
     #   break
#print(f"Negatiivsete arvude summa on {vastus}")

vastus = 0
p=int(input("Mitu korda kordame?"))
for i in range(p):
    arv = float(input("Sisesta arv: "))
    if arv < 0:
        vastus += arv
print(f"Summa on - {vastus}")


#V4 Kontrollida N inimese sisestatud isikukoodi õigsust.  
# Määrake isiku sugu. Mitu inimest N-st on mees ja mitu naissoost, ütle kasutajale.

inimesed = int(input("Sisesta inimeste arv: "))
mees = 0
naine = 0
for i in range(inimesed):
    isikukood = input("Sisesta isikukood esimene täht: ")
    if isikukood == "1" or isikukood == "3" or isikukood == "5":
        mees += 1
    elif isikukood == "2" or isikukood == "4" or isikukood == "6":
        naine += 1
    else:
        print("Vale isikukood")

print(f"Meessoost inimesi on {mees} ja naissoost inimesi on {naine}")


#V1 Koostage plokkskeem kotlette praadiva roboti jaoks.

kokku = int(input("Kokku kotlete: "))
panni_maht = int(input("Panni maht: "))
time = 1

lahendamine=kokku//panni_maht
jaak=kokku%panni_maht
if jaak>0:
    lahendamine+=1
print(f"Kokku on vaja {lahendamine} pannitäit")
for i in range(lahendamine):
    if jaak>0 and i==lahendamine-1:
        print(f"Panni peal on {jaak} kotletit")
    else:
        print(f"Panni peal on {panni_maht} kotletit")
    print(f"{i+1}. lahenemine. Praeme esimene pool")
    sleep(0.5)
    print("Umberpöörame")
    print(f"{i+1}. lahenemine. Praeme teine pool")
    sleep(0.5)
    print("Valmis")
    print()
    print("Köik kotletid on valmis")

#V8 Koostage lisatasude arvutamise algoritm: kui töötaja palk on >= 5000, on lisatasude protsent 10%; kui palk < 5000, on lisatasude protsent 12%.
while True:
    try:
        palk = float(input("Sisesta palk: "))
        break
    except ValueError:
        print("Sisestage palun number ja teine palk")

if palk >= 5000:
    lisatasu = palk * 0.1
else:
    lisatasu = palk * 0.12
print(f"Lisatasu on {lisatasu}")