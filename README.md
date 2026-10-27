# Pertemuan 13 - Debugging dan Testing

Nama: Siti Nurhasanah  
NIM: 2225250073  
Kelas: 3B

## Kasus

Program digunakan untuk mengolah data nilai mahasiswa. Program memiliki tiga fungsi utama, yaitu menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi. Pada program awal ditemukan beberapa bug yang menyebabkan hasil keluaran tidak sesuai dengan yang diharapkan.

---

## Test Case

| ID | Target | Input | Expected | Actual Awal | Status |
|----|---------|---------|---------|---------|---------|
| T1 | rata-rata | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | rata-rata | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | status | 60 | Lulus | Tidak lulus | FAIL |
| T4 | status | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | [80, 60, 90, 70] | 90 | 0 | FAIL |

---

## Bug Report

### B01 - Kesalahan Perhitungan Rata-rata

**Gejala**

Rata-rata nilai tidak sesuai dengan hasil yang seharusnya.

**Test Case**

T1 dan T2

**Lokasi**

Fungsi `hitung_rata_rata()`

**Akar Penyebab**

Program selalu membagi jumlah nilai dengan angka 5, meskipun jumlah data tidak selalu 5.

**Perbaikan**

Mengganti pembagi dari `5` menjadi `len(nilai)`.

**Retest**

PASS

---

### B02 - Kesalahan Batas Kelulusan

**Gejala**

Nilai 60 dianggap tidak lulus.

**Test Case**

T3

**Lokasi**

Fungsi `status()`

**Akar Penyebab**

Operator pembanding menggunakan `>` sehingga nilai 60 tidak memenuhi syarat kelulusan.

**Perbaikan**

Mengganti operator `>` menjadi `>=`.

**Retest**

PASS

---

### B03 - Kesalahan Pencarian Nilai Tertinggi

**Gejala**

Program menghasilkan nilai tertinggi 0.

**Test Case**

T5

**Lokasi**

Fungsi `nilai_tertinggi()`

**Akar Penyebab**

Logika perbandingan menggunakan operator `<` sehingga pencarian nilai tertinggi tidak berjalan dengan benar.

**Perbaikan**

Mengubah operator menjadi `>` dan menginisialisasi nilai awal dari elemen pertama list.

**Retest**

PASS

---

## Retest

| ID | Expected | Actual Setelah Perbaikan | Status |
|----|----------|-------------------------|---------|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

Semua test case berhasil dijalankan setelah perbaikan dan tidak ditemukan regresi pada program.

---

## Cara Menjalankan

```bash
python praktik/praktik_4_debugging.py
```

---

## Refleksi

Pada praktikum ini saya belajar bahwa program yang dapat dijalankan belum tentu menghasilkan keluaran yang benar. Dengan menggunakan test case, saya dapat menemukan bug pada fungsi rata-rata, status kelulusan, dan pencarian nilai tertinggi. Setelah melakukan perbaikan dan retest, seluruh test case berhasil dijalankan dengan hasil sesuai harapan. Teknik yang paling membantu adalah membandingkan expected result dan actual result karena dapat menunjukkan letak kesalahan program secara lebih jelas.