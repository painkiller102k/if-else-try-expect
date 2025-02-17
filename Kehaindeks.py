print("Tere, Olen sinu uus sober - Python!")
nimi = in  put("Sisesta oma nimi - ")
print(f"{nimi}, oi kui ilus nimi!")
while True:
    try:
        soov = int(input(f"{nimi}!, Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
        if soov == 1:
            print("Indeksi leidmine")
            while True:
                try:
                    pikkus = int(input("Mis on sinu pikkus? - "))
                    break
                except ValueError:
                    print("Vale pikkuse formaat!")

            while True:
                try:
                    mass = int(input("Mis on sinu mass? - "))
                    break
                except ValueError:
                    print("Vale massi formaat!")
            indeks = round(mass / (pikkus / 100) ** 2, 2)
            print(f"{nimi}, sinu keha indeks on: {indeks}")
            if indeks < 16:
                print("Tervisele ohtlik alakaal!")
            elif 16 <= indeks < 19:
                print("Alakaal!")
            elif 19 <= indeks < 25:
                print("Normaalkaal!")
            elif 25 <= indeks < 30:
                print("Ülekaal")
            elif 30 <= indeks < 35:
                print("Rasvumine")
            elif 35 <= indeks < 40:
                print("Tugev rasvumine")
            else:
                print("Tervisele ohtlik rasvumine ")
            break
        elif soov == 0:
            print("Kahju! See on vaga kasulik info!")
            break
        else:
            print("Vale valik!")
    except ValueError:
        print("Vale valiku formaat!")
        break