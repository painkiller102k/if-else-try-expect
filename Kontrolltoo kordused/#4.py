#4
while True:
    try:
        number = int(input("Sisestage naturaalarv: "))
        if number < 0:
            print("Arv peab olema positiivne")
        else:
            paariline_arv = 0
            paaritu_arv = 0
            for i in str(number):
                if int(i) % 2 == 0:
                    paariline_arv += 1
                else:
                    paaritu_arv += 1
            print(f"Arvul {number} on {paariline_arv} paarisarvu ja {paaritu_arv} paaritut arvu.")
            break
    except ValueError:
        print("Palun sisestage täisarv.")