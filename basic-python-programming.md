# Pengenalan Pemrograman Python

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

---

### Kunci Jawaban Singkat (Soal 4)

```python
celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C setara dengan {fahrenheit}°F")
```

Selamat berlatih! Pemahaman yang kuat terhadap dasar-dasar ini akan sangat membantu ketika mempelajari struktur kontrol, fungsi, dan struktur data yang lebih kompleks di Python.
