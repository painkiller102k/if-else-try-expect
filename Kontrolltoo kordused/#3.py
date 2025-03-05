import random
#3
while True:
    try:
        N = random.randint(1, 15)
        print("Juhuslik number N:", N)
        positive_arv = 0
        for i in range(N):
            number = random.randint(-15, 15)
            print("Juhuslik number:", number)
            if number > 0:
                positive_arv += 1
        print("Positiivsete arvude arv:", positive_arv)
        break
    except ValueError:
        print("Palun sisestage täisarv.")