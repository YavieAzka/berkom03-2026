# HEADER BLA BLA BLA

x = int(input("Masukkan nilai x: "))
iterasi = 0
while (x != 1):
    if (x % 2 == 0):
        x = x / 2
    else:
        x = (x * 3) + 1
    iterasi = iterasi + 1

print(f"Terjadi {iterasi} iterasi.")