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