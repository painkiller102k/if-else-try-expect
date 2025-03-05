#2
while True:
    try:
        R = int(input("Sisestage arv: "))
        if R < 0:
            print("Arv peab olema mittenegatiivne")
        else:
            product = 1
            for i in range(1, R + 1, 2):
                product *= i
            print("Kõikide paaritute arvude korrutis 0-st kuni.", R, "=", product)
            break
    except ValueError:
        print("Palun sisestage täisarv.")