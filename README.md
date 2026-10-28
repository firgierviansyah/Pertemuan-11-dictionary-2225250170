# Pertemuan 11 - Dictionary/Map

**Nama:** Firgi Erviansyah  
**NIM:** 2225250170 
**Kelas:** 3B

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Folder

```text
pertemuan-11-dictionary-NIM/
├── README.md
├── .gitignore
├── kuis.docx
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## Struktur Data

Program menggunakan dictionary dengan NIM sebagai key utama. Setiap value berupa dictionary yang menyimpan nama, kelas, dan nilai mahasiswa.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek:

```bash
python praktik/data_mahasiswa.py
```

## Test Case

| Kasus | Input/aksi | Hasil yang diharapkan |
|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan |
| Pencarian tidak tersedia | A999 | Pesan `Data tidak ditemukan` ditampilkan |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 berubah menjadi 82 |
| Penambahan data | A006 | Data mahasiswa A006 ditambahkan |
| Rekap data | `items()` | Seluruh NIM dan data mahasiswa ditampilkan |
| Rata-rata nilai | Seluruh data mahasiswa | Rata-rata nilai ditampilkan dengan benar |

## Refleksi

Dictionary memudahkan penyimpanan dan pencarian data mahasiswa berdasarkan NIM. Penggunaan `get()` membantu menangani pencarian data yang tidak tersedia tanpa menimbulkan `KeyError`. Fungsi membuat proses pencarian dan perhitungan rata-rata lebih terstruktur, sedangkan `items()` digunakan untuk menampilkan seluruh pasangan key-value.