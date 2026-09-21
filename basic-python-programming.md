# Pengenalan Pemrograman Python

Materi ini membahas dasar-dasar Python bagi pemula: tipe data, operasi aritmatika dan boolean, input & output, percabangan, perulangan, serta latihan soal untuk berlatih.

Cara me-render: ctrl/cmd + shift + s

---

## 0. Hello World!

Setiap belajar suatu bahasa pemrograman, pastikan untuk selalu mencoba "Hello World!" untuk memastikan bahasa pemrograman tersebut sudah terinstall dengan benar.

```python
print("Hello World!")
```

## 1. Tipe Data

Python memiliki beberapa tipe data dasar yang paling sering digunakan:

| Tipe Data | Contoh                         | Keterangan                                |
| --------- | ------------------------------ | ----------------------------------------- |
| `int`     | `10`, `-5`, `0`                | Bilangan bulat                            |
| `float`   | `3.14`, `-0.5`                 | Bilangan pecahan/desimal                  |
| `char`    | `'c'`, `'1'`                   | Satu karakter pada keyboard               |
| `str`     | `"Halo"`, `'Python'`           | Teks/string                               |
| `bool`    | `True`, `False`                | Nilai boolean (benar/salah)               |
| `list`    | `[1, 2, 3]`                    | Kumpulan data yang bisa diubah, berurutan |
| `tuple`   | `(1, 2, 3)`                    | Kumpulan data yang tidak bisa diubah      |
| `dict`    | `{"nama": "Budi", "umur": 20}` | Pasangan key-value                        |

### Contoh Deklarasi Variabel

```python
umur = 20              # int
tinggi = 165.5         # float
nama = "Budi"         # str
mahasiswa = True       # bool
nilai = [80, 90, 75]   # list
```

### Mengecek Tipe Data

Gunakan fungsi `type()` untuk mengecek tipe data suatu variabel:

```python
print(type(umur))     # <class 'int'>
print(type(nama))     # <class 'str'>
```

### Konversi Tipe Data (Type Casting)

```python
angka_str = "10"
angka_int = int(angka_str)     # menjadi 10 (int)

nilai_int = 7
nilai_float = float(nilai_int) # menjadi 7.0 (float)

angka = 100
angka_str = str(angka)         # menjadi "100" (str)
```

---

## 2. Operasi Aritmatika

Python mendukung operasi matematika standar berikut:

| Operator | Keterangan                       | Contoh   | Hasil |
| -------- | -------------------------------- | -------- | ----- |
| `+`      | Penjumlahan                      | `5 + 3`  | `8`   |
| `-`      | Pengurangan                      | `5 - 3`  | `2`   |
| `*`      | Perkalian                        | `5 * 3`  | `15`  |
| `/`      | Pembagian (hasil float)          | `7 / 2`  | `3.5` |
| `//`     | Pembagian bulat (floor division) | `7 // 2` | `3`   |
| `%`      | Modulus (sisa bagi)              | `7 % 2`  | `1`   |
| `**`     | Pemangkatan                      | `2 ** 3` | `8`   |

### Contoh Penggunaan

```python
a = 15
b = 4

print(a + b)   # 19
print(a - b)   # 11
print(a * b)   # 60
print(a / b)   # 3.75
print(a // b)  # 3
print(a % b)   # 3
print(a ** b)  # 50625
```

### Operator Perbandingan

Operator ini menghasilkan nilai `bool` (`True`/`False`):

| Operator | Keterangan              |
| -------- | ----------------------- |
| `==`     | Sama dengan             |
| `!=`     | Tidak sama dengan       |
| `>`      | Lebih besar dari        |
| `<`      | Lebih kecil dari        |
| `>=`     | Lebih besar sama dengan |
| `<=`     | Lebih kecil sama dengan |

```python
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 10)   # False
```

---

## 3. Operasi Boolean (Logika)

Operator logika digunakan untuk menggabungkan atau memanipulasi nilai boolean.

| Operator | Keterangan                          | Contoh           | Hasil   |
| -------- | ----------------------------------- | ---------------- | ------- |
| `and`    | Benar jika kedua kondisi benar      | `True and False` | `False` |
| `or`     | Benar jika salah satu kondisi benar | `True or False`  | `True`  |
| `not`    | Membalik nilai boolean              | `not True`       | `False` |

### Contoh Penggunaan

```python
usia = 20
punya_ktp = True

# Contoh penggunaan 'and'
boleh_memilih = usia >= 17 and punya_ktp
print(boleh_memilih)   # True

# Contoh penggunaan 'or'
libur = False
weekend = True
santai = libur or weekend
print(santai)   # True

# Contoh penggunaan 'not'
print(not weekend)   # False
```

### Kombinasi dengan Percabangan

```python
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 80 and nilai < 90:
    print("B")
else:
    print("C")
```

---

## 4. Input & Output

### Output dengan `print()`

```python
print("Selamat datang di Python!")

nama = "Budi"
umur = 20

# Menggabungkan string dan variabel
print("Nama saya", nama, "dan umur saya", umur)

# Menggunakan f-string (direkomendasikan, lebih rapi)
print(f"Nama saya {nama} dan umur saya {umur} tahun")
```

### Input dengan `input()`

Fungsi `input()` selalu mengembalikan data bertipe `str`, sehingga perlu dikonversi jika ingin diproses sebagai angka.

```python
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")

# Input berupa angka perlu di-casting
umur = int(input("Masukkan umur Anda: "))
tahun_depan = umur + 1
print(f"Tahun depan umur Anda {tahun_depan} tahun")
```

### Contoh Program Sederhana

```python
# Program menghitung luas persegi panjang
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar
print(f"Luas persegi panjang adalah {luas}")
```

---

## 5. Percabangan (if-else)

Percabangan digunakan untuk menjalankan blok kode tertentu berdasarkan suatu kondisi. Python menggunakan indentasi (spasi di awal baris) untuk menandai blok kode, bukan tanda kurung kurawal `{}` seperti bahasa lain.

### Struktur `if`

```python
umur = 17

if umur >= 17:
    print("Anda sudah boleh memiliki KTP")
```

### Struktur `if-else`

```python
nilai = 60

if nilai >= 60:
    print("Lulus")
else:
    print("Tidak Lulus")
```

### Struktur `if-elif-else`

Gunakan `elif` ("else if") ketika ada lebih dari dua kemungkinan kondisi.

```python
nilai = 75

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade D")
```

### Percabangan Bersarang (Nested If)

Percabangan bisa diletakkan di dalam percabangan lain untuk mengecek kondisi yang lebih spesifik.

```python
umur = 25
punya_sim = True

if umur >= 17:
    if punya_sim:
        print("Anda boleh berkendara")
    else:
        print("Anda perlu membuat SIM terlebih dahulu")
else:
    print("Anda belum cukup umur untuk berkendara")
```

### Catatan Penting

- Setiap blok kode di bawah `if`, `elif`, atau `else` **harus diberi indentasi** (biasanya 4 spasi), atau Python akan menampilkan error.
- Kondisi pada `if`/`elif` harus bernilai boolean (`True`/`False`), bisa langsung berupa variabel boolean atau hasil dari operator perbandingan/logika.

---

## 6. Perulangan (while & for)

Perulangan digunakan untuk mengulang eksekusi suatu blok kode beberapa kali tanpa harus menulis kode yang sama berulang-ulang.

### Perulangan `while`

`while` akan terus mengulang selama kondisinya bernilai `True`. Pastikan ada bagian dalam kode yang pada akhirnya membuat kondisi menjadi `False`, agar tidak terjadi _infinite loop_ (perulangan tanpa henti).

```python
i = 1

while i <= 5:
    print(f"Perulangan ke-{i}")
    i += 1   # penting agar loop akhirnya berhenti
```

Output:

```
Perulangan ke-1
Perulangan ke-2
Perulangan ke-3
Perulangan ke-4
Perulangan ke-5
```

### Perulangan `for`

`for` digunakan untuk mengulang sebanyak jumlah elemen pada suatu urutan (seperti `list`, `str`, atau hasil dari `range()`).

```python
# Perulangan menggunakan range()
for i in range(5):
    print(f"Angka: {i}")   # mencetak 0 sampai 4
```

`range(start, stop, step)` memiliki tiga parameter opsional:

```python
for i in range(1, 6):        # dari 1 sampai 5
    print(i)

for i in range(0, 10, 2):    # dari 0 sampai 8, loncat 2
    print(i)
```

### Perulangan pada List

```python
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(f"Saya suka {item}")
```

### `break` dan `continue`

- `break` menghentikan perulangan sepenuhnya.
- `continue` melewati iterasi saat ini dan lanjut ke iterasi berikutnya.

```python
# Contoh break
for i in range(10):
    if i == 5:
        break
    print(i)   # mencetak 0 sampai 4, lalu berhenti

# Contoh continue
for i in range(5):
    if i == 2:
        continue
    print(i)   # mencetak 0, 1, 3, 4 (angka 2 dilewati)
```

### Perulangan Bersarang (Nested Loop)

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
```

### Kapan Menggunakan `while` vs `for`?

| Situasi                                                                                         | Gunakan |
| ----------------------------------------------------------------------------------------------- | ------- |
| Jumlah perulangan sudah diketahui pasti (misal: 10 kali, atau sejumlah elemen list)             | `for`   |
| Jumlah perulangan bergantung pada suatu kondisi yang bisa berubah (misal: menunggu input valid) | `while` |

---

## 7. Latihan Soal

Cobalah kerjakan latihan berikut untuk menguji pemahaman Anda.

### Soal 1 — Tipe Data

Tebak tipe data dari nilai-nilai berikut, lalu verifikasi jawaban Anda menggunakan `type()`:

```python
a = 7
b = 7.0
c = "7"
d = True
e = [7, 8, 9]
```

### Soal 2 — Aritmatika

Buat program yang meminta pengguna memasukkan dua bilangan bulat, lalu tampilkan hasil dari operasi berikut: penjumlahan, pengurangan, perkalian, pembagian, sisa bagi, dan pemangkatan.

### Soal 3 — Boolean

Buat program yang menerima input umur pengguna, lalu menentukan apakah pengguna tersebut:

- Termasuk kategori "Balita" (0-5 tahun)
- Termasuk kategori "Anak-anak" (6-12 tahun)
- Termasuk kategori "Remaja" (13-17 tahun)
- Termasuk kategori "Dewasa" (18 tahun ke atas)

Gunakan kombinasi operator perbandingan dan boolean (`and`/`or`) sesuai kebutuhan.

### Soal 4 — Input & Output

Buat program konversi suhu sederhana:

- Minta pengguna memasukkan suhu dalam Celsius.
- Konversikan ke Fahrenheit menggunakan rumus: `F = (C * 9/5) + 32`
- Tampilkan hasilnya dengan format yang rapi menggunakan f-string.

### Soal 5 — Gabungan

Buat program kalkulator BMI (Body Mass Index) sederhana:

- Minta pengguna memasukkan berat badan (kg) dan tinggi badan (m).
- Hitung BMI menggunakan rumus: `BMI = berat / (tinggi ** 2)`
- Tampilkan kategori BMI berdasarkan hasil perhitungan:
  - BMI < 18.5 → "Kurus"
  - 18.5 <= BMI < 25 → "Normal"
  - 25 <= BMI < 30 → "Gemuk"
  - BMI >= 30 → "Obesitas"

### Soal 6 — Percabangan

Buat program yang menerima input berupa tiga sisi segitiga (a, b, c), lalu tentukan jenis segitiga tersebut:

- "Segitiga Sama Sisi" jika ketiga sisi sama panjang
- "Segitiga Sama Kaki" jika tepat dua sisi sama panjang
- "Segitiga Sembarang" jika ketiga sisi berbeda panjang

### Soal 7 — Perulangan

Buat program yang mencetak deret angka 1 sampai 100, tetapi:

- Jika angka habis dibagi 3, cetak "Fizz" (bukan angkanya).
- Jika angka habis dibagi 5, cetak "Buzz".
- Jika angka habis dibagi 3 dan 5 sekaligus, cetak "FizzBuzz".
- Selain itu, cetak angkanya seperti biasa.

(Soal ini dikenal luas sebagai "FizzBuzz" dan sering muncul dalam wawancara kerja programmer.)

### Soal 8 — Gabungan Percabangan & Perulangan

Buat program yang meminta pengguna memasukkan sebuah bilangan bulat positif, lalu tentukan apakah bilangan tersebut termasuk bilangan prima atau bukan, menggunakan perulangan `for` untuk mengecek pembagi-pembagi yang mungkin.

---

### Kunci Jawaban Singkat (Soal 4)

```python
celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C setara dengan {fahrenheit}°F")
```

### Kunci Jawaban Singkat (Soal 7 — FizzBuzz)

```python
for angka in range(1, 101):
    if angka % 3 == 0 and angka % 5 == 0:
        print("FizzBuzz")
    elif angka % 3 == 0:
        print("Fizz")
    elif angka % 5 == 0:
        print("Buzz")
    else:
        print(angka)
```

Selamat berlatih! Pemahaman yang kuat terhadap dasar-dasar ini akan sangat membantu ketika mempelajari fungsi dan struktur data yang lebih kompleks di Python.# Pengenalan Pemrograman Python

Materi ini membahas dasar-dasar Python bagi pemula: tipe data, operasi aritmatika dan boolean, input & output, serta latihan soal untuk berlatih.

Cara me-render: ctrl/cmd + shift + s

---

## 0. Hello World!

Setiap belajar suatu bahasa pemrograman, pastikan untuk selalu mencoba "Hello World!" untuk memastikan bahasa pemrograman tersebut sudah terinstall dengan benar.

```python
print("Hello World!")
```

## 1. Tipe Data

Python memiliki beberapa tipe data dasar yang paling sering digunakan:

| Tipe Data | Contoh                         | Keterangan                                |
| --------- | ------------------------------ | ----------------------------------------- |
| `int`     | `10`, `-5`, `0`                | Bilangan bulat                            |
| `float`   | `3.14`, `-0.5`                 | Bilangan pecahan/desimal                  |
| `char`    | `'c'`, `'1'`                   | Satu karakter pada keyboard               |
| `str`     | `"Halo"`, `'Python'`           | Teks/string                               |
| `bool`    | `True`, `False`                | Nilai boolean (benar/salah)               |
| `list`    | `[1, 2, 3]`                    | Kumpulan data yang bisa diubah, berurutan |
| `tuple`   | `(1, 2, 3)`                    | Kumpulan data yang tidak bisa diubah      |
| `dict`    | `{"nama": "Budi", "umur": 20}` | Pasangan key-value                        |

### Contoh Deklarasi Variabel

```python
umur = 20              # int
tinggi = 165.5         # float
nama = "Budi"         # str
mahasiswa = True       # bool
nilai = [80, 90, 75]   # list
```

### Mengecek Tipe Data

Gunakan fungsi `type()` untuk mengecek tipe data suatu variabel:

```python
print(type(umur))     # <class 'int'>
print(type(nama))     # <class 'str'>
```

### Konversi Tipe Data (Type Casting)

```python
angka_str = "10"
angka_int = int(angka_str)     # menjadi 10 (int)

nilai_int = 7
nilai_float = float(nilai_int) # menjadi 7.0 (float)

angka = 100
angka_str = str(angka)         # menjadi "100" (str)
```

---

## 2. Operasi Aritmatika

Python mendukung operasi matematika standar berikut:

| Operator | Keterangan                       | Contoh   | Hasil |
| -------- | -------------------------------- | -------- | ----- |
| `+`      | Penjumlahan                      | `5 + 3`  | `8`   |
| `-`      | Pengurangan                      | `5 - 3`  | `2`   |
| `*`      | Perkalian                        | `5 * 3`  | `15`  |
| `/`      | Pembagian (hasil float)          | `7 / 2`  | `3.5` |
| `//`     | Pembagian bulat (floor division) | `7 // 2` | `3`   |
| `%`      | Modulus (sisa bagi)              | `7 % 2`  | `1`   |
| `**`     | Pemangkatan                      | `2 ** 3` | `8`   |

### Contoh Penggunaan

```python
a = 15
b = 4

print(a + b)   # 19
print(a - b)   # 11
print(a * b)   # 60
print(a / b)   # 3.75
print(a // b)  # 3
print(a % b)   # 3
print(a ** b)  # 50625
```

### Operator Perbandingan

Operator ini menghasilkan nilai `bool` (`True`/`False`):

| Operator | Keterangan              |
| -------- | ----------------------- |
| `==`     | Sama dengan             |
| `!=`     | Tidak sama dengan       |
| `>`      | Lebih besar dari        |
| `<`      | Lebih kecil dari        |
| `>=`     | Lebih besar sama dengan |
| `<=`     | Lebih kecil sama dengan |

```python
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 10)   # False
```

---

## 3. Operasi Boolean (Logika)

Operator logika digunakan untuk menggabungkan atau memanipulasi nilai boolean.

| Operator | Keterangan                          | Contoh           | Hasil   |
| -------- | ----------------------------------- | ---------------- | ------- |
| `and`    | Benar jika kedua kondisi benar      | `True and False` | `False` |
| `or`     | Benar jika salah satu kondisi benar | `True or False`  | `True`  |
| `not`    | Membalik nilai boolean              | `not True`       | `False` |

### Contoh Penggunaan

```python
usia = 20
punya_ktp = True

# Contoh penggunaan 'and'
boleh_memilih = usia >= 17 and punya_ktp
print(boleh_memilih)   # True

# Contoh penggunaan 'or'
libur = False
weekend = True
santai = libur or weekend
print(santai)   # True

# Contoh penggunaan 'not'
print(not weekend)   # False
```

### Kombinasi dengan Percabangan

```python
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 80 and nilai < 90:
    print("B")
else:
    print("C")
```

---

## 4. Input & Output

### Output dengan `print()`

```python
print("Selamat datang di Python!")

nama = "Budi"
umur = 20

# Menggabungkan string dan variabel
print("Nama saya", nama, "dan umur saya", umur)

# Menggunakan f-string (direkomendasikan, lebih rapi)
print(f"Nama saya {nama} dan umur saya {umur} tahun")
```

### Input dengan `input()`

Fungsi `input()` selalu mengembalikan data bertipe `str`, sehingga perlu dikonversi jika ingin diproses sebagai angka.

```python
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")

# Input berupa angka perlu di-casting
umur = int(input("Masukkan umur Anda: "))
tahun_depan = umur + 1
print(f"Tahun depan umur Anda {tahun_depan} tahun")
```

### Contoh Program Sederhana

```python
# Program menghitung luas persegi panjang
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar
print(f"Luas persegi panjang adalah {luas}")
```

---

## 5. Latihan Soal

Cobalah kerjakan latihan berikut untuk menguji pemahaman Anda.

### Soal 1 — Tipe Data

Tebak tipe data dari nilai-nilai berikut, lalu verifikasi jawaban Anda menggunakan `type()`:

```python
a = 7
b = 7.0
c = "7"
d = True
e = [7, 8, 9]
```

### Soal 2 — Aritmatika

Buat program yang meminta pengguna memasukkan dua bilangan bulat, lalu tampilkan hasil dari operasi berikut: penjumlahan, pengurangan, perkalian, pembagian, sisa bagi, dan pemangkatan.

### Soal 3 — Boolean

Buat program yang menerima input umur pengguna, lalu menentukan apakah pengguna tersebut:

- Termasuk kategori "Balita" (0-5 tahun)
- Termasuk kategori "Anak-anak" (6-12 tahun)
- Termasuk kategori "Remaja" (13-17 tahun)
- Termasuk kategori "Dewasa" (18 tahun ke atas)

Gunakan kombinasi operator perbandingan dan boolean (`and`/`or`) sesuai kebutuhan.

### Soal 5 — Input & Output

Buat program konversi suhu sederhana:

- Minta pengguna memasukkanius.
- Konversikan ke Fahrenheit menggunakan rumus: `F = (C * 9/5) + 32`
- Tampilkan hasilnya dengan format yang rapi menggunakan f-string.

### Soal 5 — Gabungan

Buat program kalkulator BMI (Body Mass Index) sederhana:

- Minta pengguna memasukkan berat badan (kg) dan tinggi badan (m).
- Hitung BMI menggunakan rumus: `BMI = berat / (tinggi ** 2)`
- Tampilkan kategori BMI berdasarkan hasil perhitungan:
  - BMI < 18.5 → "Kurus"
  - 18.5 <= BMI < 25 → "Normal"
  - 25 <= BMI < 30 → "Gemuk"
  - BMI >= 30 → "Obesitas"

---

### Kunci Jawaban Singkat (Soal 4)

```python
celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C setara dengan {fahrenheit}°F")
```
