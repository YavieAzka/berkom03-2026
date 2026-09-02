print("Hello World")

# halo apa kabar

# Variabel
umur = 20
print(umur)
# Penamaan Variabel TIDAK BOLEH pakai spasi

# String harus pake ""
nama_saya = "Andi"
#   |         |
# variabel  value
print(nama_saya)

nama_saya = umur
print(nama_saya)

# Typecasting : perubahan tipe data suatu variabel

angka_int = 1
angka_str = str(1) # 1 -> "1"

# No. Telp : 621233454536
# Kapan pakai int: operasi matematika
# Nama | No.Telp

# Operasi aritmetika
indeks_mat = 3.5
sks_mat = 4
indeks_kim = 3.75
sks_kim = 3
indeks_berkom = 4
sks_berkom = 3

jumlah_nilai = (indeks_mat * sks_mat) + (indeks_kim * sks_kim) + (indeks_berkom * sks_berkom)
ip_final = jumlah_nilai / (sks_mat + sks_kim + sks_berkom)

print("Nilai IP final adalah: ", ip_final)

# Input & Output
# Input HARUS selalu disimpan di sebuah variabel

# Contoh: Program kalkulator untuk menjumlahkan 2 bilangan
print("== Kalkulator ==")
angka_1 = int(input("Masukkan angka pertama: "))
angka_2 = int(input("Masukkan angka kedua: "))

hasil = angka_1 + angka_2
print(f"Hasil dari {angka_1} + {angka_2} = {hasil}")
