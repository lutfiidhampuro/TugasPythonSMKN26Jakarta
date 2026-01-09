# 1. Fungsi untuk menghitung luas lingkaran
def luas_lingkaran(r):
    return 3.14 * r**2

# 2. Fungsi untuk menghitung nilai akhir (rata-rata dari tugas, UTS, dan UAS)
def nilai_akhir(tugas, uts, uas):
    return (tugas + uts + uas) / 3

# 3. Fungsi untuk mengonversi suhu Celcius ke Fahrenheit
def konversi_suhu(celcius):
    return (9/5 * celcius) + 32

# 4. Fungsi untuk menampilkan info siswa
def info_siswa(nama, kelas="X SIJA"):
    print(f"Nama  : {nama}")
    print(f"Kelas : {kelas}")
    print("-" * 20)

# 5. Lambda function untuk menghitung kuadrat dari suatu angka
kuadrat = lambda x: x**2

# Menampilkan Output
print("=== Fungsi Luas Lingkaran ===")
print("Luas lingkaran (r=7):", luas_lingkaran(7))
print("=== Fungsi Luas Lingkaran selesai ===")

print("")
print("=== Fungsi menghitung nilai akhir ===")
print("Nilai akhir:", nilai_akhir(80, 75, 90))
print("=== Fungsi menghitung nilai akhir selesai ===")

print("")
print("=== Fungsi mengkonversi Fahrenheit ke Celcius ===")
print("Suhu Fahrenheit dari 30°C:", konversi_suhu(30))
print("=== Fungsi mengkonversi Fahrenheit ke Celcius selesai ===")

print("")
print("=== Fungsi menampilkan info siswa ===")
info_siswa("Lutfi Idham")
info_siswa("Azriel Agrin Oktafiansyah")
info_siswa("Dwi Saputra")
print("=== Fungsi menampilkan info siswa selesai ===")

print("")
print("=== Lambda function ===")
print("Kuadrat dari 5:", kuadrat(5))
print("=== Lambda function selesai ===")