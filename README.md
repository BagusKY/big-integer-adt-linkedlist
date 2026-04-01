# Big Integer ADT Implementation (Linked List & Python List)

## 📌 Deskripsi

Proyek ini merupakan implementasi **Abstract Data Type (ADT) BigInteger** menggunakan dua pendekatan struktur data:

1. **Singly Linked List**
2. **Python List (Array)**

BigInteger digunakan untuk merepresentasikan bilangan bulat dengan ukuran sangat besar yang melebihi batas tipe data bawaan.

---

## 🎯 Tujuan Praktikum

* Memahami konsep **Abstract Data Type (ADT)**
* Mengimplementasikan bilangan besar tanpa menggunakan tipe `int` bawaan
* Melatih manipulasi data berbasis:

  * Linked List
  * Array/List
* Mengimplementasikan operasi:

  * Representasi string
  * Perbandingan
  * Operasi aritmatika
  * Operasi bitwise

---

## 🧠 Konsep Utama

### 🔹 Representasi Data

Bilangan disimpan sebagai kumpulan digit:

* Setiap node / elemen menyimpan **1 digit (0–9)**
* Urutan penyimpanan:

  * **LSD (Least Significant Digit) → MSD (Most Significant Digit)**

Contoh:
123 disimpan sebagai:

```
3 → 2 → 1
```

---

## 🧩 Struktur Project

```
big-integer-adt-linkedlist/
│
├── README.md
├── main.py
│
├── bigint/
│   ├── __init__.py
│   ├── bigint_base.py
│   ├── bigint_linkedlist.py
│   ├── bigint_list.py
│
├── linkedlist/
│   ├── node.py
│   ├── singly_linked_list.py
│
├── utils/
│   ├── helper.py
│
├── tests/
│   ├── test_bigint_linkedlist.py
│   ├── test_bigint_list.py
```

---

## ⚙️ Fitur Utama

### 1. Representasi

* `toString()` → Mengubah BigInteger ke string

### 2. Perbandingan

* `comparable(other)`

  * -1 → lebih kecil
  * 0 → sama
  * 1 → lebih besar

### 3. Operasi Aritmatika

Melalui:

```
arithmetic(other, op)
```

Operator yang didukung:

* `+` → penjumlahan
* `-` → pengurangan
* `*` → perkalian

---

### 4. Operasi Bitwise (Basic)

Melalui:

```
bitwise(other, op)
```

Operator:

* `&` → AND
* `|` → OR
* `^` → XOR

> Catatan: Implementasi bitwise saat ini masih menggunakan pendekatan konversi numerik dan dapat dikembangkan menjadi full binary-based.

---

## 🆚 Perbandingan Pendekatan

| Aspek        | Linked List             | Python List      |
| ------------ | ----------------------- | ---------------- |
| Struktur     | Node + pointer          | Array (index)    |
| Akses data   | Sequential              | Random access    |
| Kompleksitas | Lebih kompleks          | Lebih sederhana  |
| Pembelajaran | Pointer & struktur data | Manipulasi array |

---

## ▶️ Cara Menjalankan Program

### Jalankan Demo

```
python main.py
```

---

### Jalankan Testing

```
python -m unittest tests/test_bigint_linkedlist.py
python -m unittest tests/test_bigint_list.py
```

---

## 🧪 Contoh Output

```
=== BIGINTEGER (LINKED LIST) ===
A = 45839
B = 12345
A + B = 58184
A - B = 33494
A * B = 566232955

=== BIGINTEGER (PYTHON LIST) ===
X = 45839
Y = 12345
X + Y = 58184
```

---

## ⚠️ Keterbatasan Saat Ini

* Operasi `//`, `%`, dan `**` belum diimplementasikan
* Bitwise masih menggunakan konversi bawaan (belum full ADT)
* Belum mendukung bilangan negatif

---

## 🚀 Pengembangan Lanjutan

* Implementasi:

  * Pembagian (`//`)
  * Modulus (`%`)
  * Pangkat (`**`)
* Bitwise berbasis binary tanpa `int`
* Optimasi linked list (tail pointer)
* Benchmark performa (LinkedList vs List)

---

## 👨‍💻 Author

Nama: M. Bagus Kuncoro Yekti

Mata Kuliah: Struktur Data

Topik: BigInteger ADT Implementation

---

## 📚 Kesimpulan

Proyek ini menunjukkan bahwa:

* Struktur data sederhana dapat digunakan untuk menyelesaikan masalah kompleks
* Representasi data sangat mempengaruhi algoritma
* ADT memisahkan **konsep** dari **implementasi**

---
