h = int(input())
mulai = h
selesai = h
for i in range (1, h + 1):
    angka = h
    for j in range (1, h*2):
        if(j >= mulai and j <= selesai):
            print(angka, end=' ')
            if(j < h): angka = angka - 1
            else: angka = angka + 1
        else:
            print(" ", end=' ')
        
    mulai = mulai - 1
    selesai = selesai + 1
    print("")

mulai = mulai + 2
selesai = selesai - 2

for i in range (1, h + 1):
    angka = h
    for j in range (1, h*2):
        if(j >= mulai and j <= selesai):
            print(angka, end=' ')
            if(j < h): angka = angka - 1
            else: angka = angka + 1
        else:
            print(" ", end=' ')
        
    mulai = mulai + 1
    selesai = selesai - 1
    print("")
