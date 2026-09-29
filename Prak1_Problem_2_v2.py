n = int(input("Masukkan sebuah bilangan: "))

'''
m = 2489 -> 2, 4, 8, 9
n = 9654 -> 9, 6, 5, 4

Modulo dan Pembagian
2  4  8  9
Angka 4: n % 10
Angka 3: (n // 10) % 10
Angka 2: (n // 100) % 10
Angka 1: (n // 1000)

2489 -> 24 89
        b1 b2
b1 = angka_1 * 10 + angka_2
b2 = angka_3 * 10 + angka 4

'''

angka_4 = n % 10
angka_3 = (n // 10) % 10
angka_2 = (n // 100) % 10
angka_1 = (n // 1000)

b1 = angka_1 * 10 + angka_2
b2 = angka_3 * 10 + angka_4

# Cek gamma duluan
if ((angka_1 > angka_2 and angka_2 > angka_3 and angka_3 > angka_4) or (angka_1 < angka_2 and angka_2 < angka_3 and angka_3 < angka_4) and (b1 - b2 >= 30)):
    print("Bilangan tersebut adalah bilangan gamma.")

# Cek alfa
elif ((angka_1 > angka_2 and angka_2 > angka_3 and angka_3 > angka_4) or (angka_1 < angka_2 and angka_2 < angka_3 and angka_3 < angka_4)):
    print("Bilangan tersebut adalah bilangan alfa.")

# Cek Beta
elif (b1 - b2 >= 30):
    print("Bilangan tersebut adalah bilangan beta.")

else:
    print("Bilangan tersebut adalah bilangan delta.")





