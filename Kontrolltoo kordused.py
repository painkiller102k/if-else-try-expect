import random
#1
while True:
    try:
        a = int(input("Sisestage number vahemikus 1 kuni 9: "))
        if a < 1 or a > 9:
            print("Number peab olema vahemikus 1-9")
        else:
            for i in range(4):
                if i == 0:
                    for i in range(a):
                        print("    /V\\    ", end=" ")
                    print()
                elif i == 1:
                    for i in range(a):
                        print("   / V \\   ", end=" ")
                    print()
                elif i == 2:
                    for i in range(a):
                        print("  / V V \\  ", end=" ")
                    print()
                elif i == 3:
                    for i in range(a):
                        print(" /VV V VV\\ ", end=" ")
                    print()
            break
    except ValueError:
        print("Palun sisestage täisarv.")



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

#3
while True:
    try:
        N = random.randint(1, 15)
        print("Juhuslik number N:", N)
        count_positive = 0
        for i in range(N):
            number = random.randint(-15, 15)
            print("Juhuslik number:", number)
            if number > 0:
                count_positive += 1
        print("Positiivsete arvude arv:", count_positive)
        break
    except ValueError:
        print("Palun sisestage täisarv.")

#4
while True:
    try:
        number = int(input("Sisestage naturaalarv: "))
        if number < 0:
            print("Arv peab olema positiivne")
        else:
            paariline_arv = 0
            paaritu_arv = 0
            for arv in str(number):
                if int(arv) % 2 == 0:
                    paariline_arv += 1
                else:
                    paaritu_arv += 1
            print(f"Arvul {number} on {paariline_arv} paarisarvu ja {paaritu_arv} paaritut arvu.")
            break
    except ValueError:
        print("Palun sisestage täisarv.")

#5
while True:
    try:
        A = int(input("Sisestage arv A: "))
        B = int(input("Sisestage arv B: "))
        if A > B:
            print("A peab olema väiksem või võrdne B-ga")
        else:
            summa = 0
            for i in range(A, B + 1):
                summa += i
            print(f"Summa arvude vahemikus {A} kuni {B} on {summa}.")
            break
    except ValueError:
        print("Palun sisestage täisarv.")