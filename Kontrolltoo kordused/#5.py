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