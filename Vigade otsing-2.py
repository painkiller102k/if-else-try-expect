print("*** Arvude mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))) # )
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga on möttetu töö")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu paarilist ja mitu paaritut numbrit on numbris.")
    print()
    c=b=a # ---> c=b=a
    paaris = 0 # ---> =
    paaritu = 0 # ---> =
while b > 0: # ---> : 
            if b % 2 == 0: # ----> ==
                    paaris =+ 1
            else:
                    paaritu =+ 1
                    b = b // 10
    
print("Paarisarvud:",paaris) # ----> ,paaris
print("Paarituarvud:",paaritu) # ----> ,paaritu
print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*Pöörake* sisestatud number ümber")
print()
b=0
while a > 0: # ----> :
          number = a % 10
          a = a // 10
          b = b * 10
          b =+ number
print("*Pöörake* arv'", b)
print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Syracuse'i hüpoteesi testimine.") # ---> (
print()
if c % 2 == 0: # ---> ==
    print("c on paariline arv. Jagage 2ga.")
else:
    print("c on paaritu arv. Korrutage 3, lisage 1 ja jagage 2ga.")
    while c != 1:
            if c % 2 == 0: # ---> ==
                    c == c / 2
            else:
                    c == (3*c + 1) / 2
            print("c", end="") # ----> "c" ----> end=""
    print()
    print("Hüpotees on õige.") # ---> ""