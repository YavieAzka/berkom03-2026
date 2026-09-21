# Program untuk mengategorikan rentang umur seseorang
# 0 - 5 : Balita
# 6 - 12 : Anak-anak
# 12 - 17 : Remaja
# > 18: Dewasa
'''
umur = int(input("Masukkan umur: "))

if(umur < 0):
    print("Umur tidak valid!")
elif(umur >= 0 and umur <= 5):
    print("Balita")
elif(umur >= 6 and umur <= 12):
    print("Anak-anak")
elif(umur >= 12 and umur < 18):
    print("Remaja")
elif(umur >= 18):
    print("Dewasa")
'''
'''
hujan = False
gempa_maha_dahsyat = True

if(hujan):
    kuliah = False
else:
    kuliah = True
print(kuliah)
'''

# Program untuk menentukan sebuah bilangan merupakan ganjil/genap/desimal
angka = float(input("Masukkan suatu angka: "))
if(angka % 2 == 0):
    print("Genap")
elif(angka % 2 == 1):
    print("Ganjil")
else:
    print("Desimal")


# Program untuk mengecek apakah suatu tahun kabisat atau tidak
# Habis dibagi 400 -> kabisat 
# habis dibagi 100, tapi tidak habis dibagi 400 -> tidak kabisat
# habis dibagi 4, tapi tidak habis dibagi 100 -> kabisat
'''
tahun = int(input("Masukkan tahun: "))

if(tahun % 400 == 0):
    print("Kabisat")

elif(tahun % 100 == 0 and tahun % 400 != 0):
    print("Tidak kabisat")

elif(tahun % 4 == 0 and tahun % 100 != 0):
    print("Kabisat")
'''

