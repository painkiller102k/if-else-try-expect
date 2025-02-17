import math
### Ülesanne 1
valik = input("Valige kujund (1 - ruut, 2 - ristkülik, 3 - ring) => ")

if valik == "1":
    try:
        a = float(input('Sisestage ruudu küljepikkus => '))
        if a > 0:
            S = a**2
            print("Nelinurkne pindala:", S)
            P = 4 * a
            print("Ruudu ümbermõõt:", P)
            di = a * math.sqrt(2)
            print("Ruutdiagonaal:", round(di, 2))
        elif a <= 0:
            print("Viga, sisestage positiivne number")
    except ValueError:
        print("Viga, sisestage kehtiv number!")

elif valik == "2":
    try:
        b = float(input("Sisestage ristküliku esimese külje pikkus => "))
        c = float(input("Sisestage ristküliku teise külje pikkus => "))
        if b > 0:
            S = b * c
            print("Ristküliku pindala:", S)
            P = 2 * (b + c)
            print("Ristküliku ümbermõõt:", P)
            di = math.sqrt(b**2 + c**2)
            print("Ristkülikukujuline diagonaal:", round(di, 2))
        elif b <= 0:
            print("Viga, sisestage positiivne number!")
        if c > 0:
            S = b * c
            print("Ristküliku pindala:", S)
            P = 2 * (b + c)
            print("Ristküliku ümbermõõt:", P)
            di = math.sqrt(b**2 + c**2)
            print("Ristkülikukujuline diagonaal:", round(di, 2))
        elif c <= 0:
            print("Viga, sisestage positiivne number!")
    except ValueError:
        print("Viga, sisestage kehtiv number!")

elif valik == "3":
    try:
        r = float(input('Sisestage ringi raadius => '))
        if r > 0:
            d = 2 * r
            print("Ringi läbimõõt:", d)
            S = math.pi * r**2
            print("Ringi ala:", round(S, 2))
            C = 2 * math.pi * r
            print("Ümbermõõt:", round(C, 2))
        elif r <= 0:
            print("Viga, sisestage positiivne number!")
    except ValueError:
        print("Viga, sisestage kehtiv number!")

else:
    print("Viga, valige 1, 2 või 3!")