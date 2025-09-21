nama = input("Masukkan nama Anda: ")
berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan Anda (cm): "))

# Konversi tinggi dari cm ke meter
tinggi_m = tinggi_cm / 100

# Hitung IMT
imt = berat / (tinggi_m ** 2)

# Tentukan kategori IMT
if imt < 18.5:
    kategori = "Kurus"
elif 18.5 <= imt <= 24.9:
    kategori = "Normal"
elif 25 <= imt <= 29.9:
    kategori = "Kelebihan Berat"
else:
    kategori = "Obesitas"

# Tampilkan hasil
print(f"{nama}, IMT Anda adalah {imt:.2f}")
print(f"Kategori berat badan Anda: {kategori}")
