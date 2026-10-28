def cari_mahasiswa(data, nim):
    return data.get(nim)


def rata_rata_nilai(data):
    total = 0

    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Edo", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# Pencarian mahasiswa
nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(nim, hasil)
else:
    print("Data tidak ditemukan")

# Pencarian NIM yang tidak tersedia
nim = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(nim, hasil)
else:
    print("Data tidak ditemukan")

# Menambahkan mahasiswa baru
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

# Memperbarui nilai mahasiswa
data_mahasiswa["A002"]["nilai"] = 82

# Menampilkan seluruh data mahasiswa
for nim, mahasiswa in data_mahasiswa.items():
    print(nim, mahasiswa)

# Menghitung rata-rata nilai
print("Rata-rata nilai:", rata_rata_nilai(data_mahasiswa))