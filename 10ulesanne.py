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