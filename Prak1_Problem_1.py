kuis_1 = float(input("Masukkan nilai kuis pertama: "))
kuis_2 = float(input("Masukkan nilai kuis kedua: "))
kuis_3 = float(input("Masukkan nilai kuis ketiga: "))

rata_rata = (kuis_1 + kuis_2 + kuis_3) / 3

if (rata_rata >= 80):
    print("Tuan Kil mendapatkan nilai Lulus Memuaskan.")
elif (rata_rata >= 70):
    print("Tuan Kil mendapatkan nilai Lulus")
else:
    print("Tuan Kil mendapatkan nilai Tidak Lulus.")