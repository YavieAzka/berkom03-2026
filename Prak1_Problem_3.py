
# PROGRAM
# Judul Program :
# Deskripsi Program: program untuk menghitung biaya pengiriman
 
# KAMUS
# metode_pengiriman : string
# banyak_barang : int

# ALGORITMA
metode_pengiriman = str(input("Metode pengiriman barang: "))

if (metode_pengiriman == "reguler" or metode_pengiriman == "kilat"):
    banyak_barang = int(input("Masukkan banyaknya barang: "))
    berat_barang = int(input("Masukkan total berat barang (dalam kg): "))

    total_biaya = 0

    if (metode_pengiriman == "reguler"):
        total_biaya = total_biaya + 15000
        total_biaya = total_biaya + (5000 * berat_barang)
        if (berat_barang > 10):
            total_biaya = total_biaya + (berat_barang - 10) * 2000
        if (banyak_barang > 4):
            total_biaya = total_biaya * 0.9
        print("Diperlukan biaya pengiriman sebesar", total_biaya)

    elif (metode_pengiriman == "kilat"):
        if (banyak_barang >= 2):
            total_biaya = total_biaya + 15000
            total_biaya = total_biaya + (9000 * berat_barang)
            if (berat_barang > 10):
                total_biaya = total_biaya + (berat_barang - 10) * 2000
            if (banyak_barang > 4):
                total_biaya = total_biaya * 0.85
            print("Diperlukan biaya pengiriman sebesar ", total_biaya)
        else:
            print("Pengiriman tidak dapat dilakukan.")

else: 
    print("Metode pengiriman tidak valid!")