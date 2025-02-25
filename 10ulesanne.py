import random
#1
# k = 0
# for i in range(15):
#     while True:
#         try:
#             arv = float(input(f"Sisesta {i+1} arv: "))
#             break
#         except ValueError:
#             print("Palun sisesta ainult numbrid.")
#    print(i)
#    if arv == int(arv):
#        k += 1
#print(f"Kokku oli {k} täisarvu.")

#2
# try:
#     A = int(input("Sisesta arv A: "))
#     if A < 1:
#         print("Palun sisesta positiivne täisarv.")
#     else:
#         summa = sum(range(1, A + 1))
#         print(f"Kõikide naturaalarvude summa vahemikus 1 kuni {A} on {summa}.")
# except ValueError:
#     print("Palun sisesta ainult täisarv.")

#3
# summa = 0
# for i in range(8):
#     while 1:
#         try:
#             B = int(input(f"Sisesta {i+1} arv: "))
#             break
#         except ValueError:
#             print("Palun sisesta ainult täisarv.")
#     if B > 0:
#         summa += B
# print(f"Positiivsete arvude summa on {summa}.")

#4
# for i in range(10, 21):
#     print(f"{i}^2 = {i**2}")

#5
# summ = 0
# N = 0
# while True:
#     try:
#         N = int(input("Sisesta arv N: "))
#         break
#     except ValueError:
#         print("Palun sisesta ainult täisarv.")
# for i in range(N):
#     while True:
#         try:
#             arv = int(input(f"Sisesta {i+1} arv: "))
#             break
#         except ValueError:
#             print("Palun sisesta ainult täisarv.")
#     if arv < 0:
#         summ += arv
# print(f"Negatiivsete arvude summa on {summ}.")

#6

# try:
#     N = int(input("Sisesta arv N: "))
# except ValueError:
#     print("Palun sisesta ainult täisarv.")

# negatiivsed = 0
# positiivsed = 0
# nullid = 0

# for i in range(N):
#     while True:
#         try:
#             arv = int(input(f"Sisesta {i+1} arv: "))
#             break
#         except ValueError:
#             print("Palun sisesta ainult täisarv.")
    
#     if arv < 0:
#         negatiivsed += 1
#     elif arv > 0:
#         positiivsed += 1
#     else:
#         nullid += 1

# print(f"Negatiivsete arvude arv: {negatiivsed}")
# print(f"Positiivsete arvude arv: {positiivsed}")
# print(f"Nullide arv: {nullid}")

#7
# while True:
#     try:
#         multiplicative = int(input("Sisesta arv: "))
#         intermediateStart = int(input("Sisesta arv Start: "))
#         intermediateEnd = int(input("Sisesta arv End: "))
#         break
#     except ValueError:
#         print("Palun sisesta ainult täisarv.")
# for i in range(intermediateStart, intermediateEnd + 1):
#     if i % multiplicative == 0:
#         print(i)

#8
# while True:
#     try:
#         inch = float(input("Sisesta inch: "))
#         cm = inch * 2.54
#         if 1 < inch < 20:
#             print(f"{inch} tolli on {cm} cm.")
#             break
#         else:
#             print("Palun sisesta arv vahemikus 1 kuni 20.")
#     except ValueError:
#         print("Palun sisesta arv vahemikus 1 kuni 20.")

#9
# while True:
#     try:
#         raha = float(input("Sisesta raha: "))
#         years = int(input("Sisesta aastad: "))
#     except ValueError:
#         print("Palun sisesta ainult numbrid.")
#     else:
#         break

# for i in range(years):
#     raha = raha * 1.03
# print(f"Summa {years} aasta pärast on {round((raha), 2)} Euro.")



#22
# summs = 0
# for i in range(100, 201):
#     if i % 17 == 0:
#         summs += i
# print(summs)
# Ul 20
# sum = 0
# for i in range(20, 51):
#     if i % 5 or i % 7 == 0:
#         sum += i
# print(sum)

#11
random_number = random.randint(1, 9)
print(f"Случайное число: {random_number}")

product = 1
found = False
for i in range(10, 100):
    if i % 2 != 0 and i % random_number == 0:
        product *= i
        found = True

if found:
    print(f"Произведение двузначных нечетных чисел, кратных {random_number}: {product}")
else:
    print(f"Нет двузначных нечетных чисел, кратных {random_number}")

#12
n = int(input("Введите количество сенокосилок: "))
n2 = int(input("Введите количество часов работы первой сенокосилки: "))

a = 10 / 60

total_hours = 0
for i in range(n):
    total_hours += n2 + i * a

print(f"Общее количество часов, проработанных всей бригадой: {total_hours}")

#13
count = 0
total_sum = 0

for i in range(100, 1000):
    if i % 7 == 0:
        count += 1
        total_sum += i

print(f"Количество чисел, кратных 7: {count}")
print(f"Сумма чисел, кратных 7: {total_sum}")

#15
for i in range(10):
    for i in range(10):
        print(i, end=' ')
    print()

#16
for i in range(1, 10):
    for h in range(9):
        if h == i - 1:
            print(i, end=' ')
        else:
            print(0, end=' ')
    print()

#17
for i in range(1, 10):
    print(f"2*{i}={2*i}")

#18
for i in range(20, 50):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

#19
for i in range(35, 87):
    if i % 7 in (1, 2, 5):
        print(i)

#29
for i in range(9): 
    for h in range(9):
        if h == 0 or h == i:
            print('x', end=' ')
        else:
            print('0', end=' ')
    print()

#30
M = random.randint(1, 100)
N = random.randint(1, 100)

print(f"Сгенерированные числа: M = {M}, N = {N}")

if N > M:
    print("Последовательность от N к M:")
    for i in range(N, M - 1, -1):
        print(i)
else:
    print("Последовательность от N к M:")
    for i in range(N, M + 1):
        print(i)

print()
if M > N:
    print("Последовательность от M к N:")
    for i in range(M, N - 1, -1):
        print(i)
else:
    print("Последовательность от M к N:")
    for i in range(M, N + 1):
        print(i)