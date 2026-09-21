# While
'''
pesan = str(input("(user) "))
while(pesan != "exit"):
    print("(bot) ", pesan)
    pesan = str(input("(user) "))
'''
# input : sebuah bilangan (n)
# output: tampilkan hasil 1 + 2 + ... + n

n = int(input("Masukkan sebuah angka: "))
hasil = 0
i = 1
while(i <= n):
    hasil = hasil + i
    i = i + 1 # increment

print("Hasil dari 1 + 2 + ... + n adalah ", hasil)

# perbedaan = dan ==
# a = b : nilai 'a' diisi dengan 'b'
# a == b : apakah a = b? (true/false)
# a != b : apakah a tidak sama dengan b? (true/false)

# mencari nilai faktorial
hasil = 1
i = 1
while(i <= n):
    hasil = hasil * i
    i = i + 1 # increment

print("Hasil dari faktorial n adalah ", hasil)

