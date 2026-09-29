# PROGRAM ...
# KAMUS ...

# ALGORITMA

n = int(input("Masukkan banyak nilai: "))
terkecil_1 = 999999
terkecil_2 = 999999

for i in range (1, n + 1):
    nilai = int(input(f"Masukkan nilai ke-{i}: "))
    if (i == 1):
        terkecil_1 = nilai
    elif (i == 2):
        if (nilai < terkecil_1):
            terkecil_2 = terkecil_1
            terkecil_1 = nilai
        else:
            terkecil_2 = nilai
    else:
        if (nilai < terkecil_1):
            terkecil_1 = nilai
        else:
            if (nilai < terkecil_2):
                terkecil_2 = nilai

rata_rata = (terkecil_1 + terkecil_2) / 2
print("Rata -rata 2 nilai terkecil adalah ", rata_rata)


