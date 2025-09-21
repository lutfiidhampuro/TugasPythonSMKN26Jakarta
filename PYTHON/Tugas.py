print("=== Program Hitung Luas Bangun Datar ===")
print("1. Persegi Panjang")
print("2. Segitiga")

pilih = int(input("Pilih bangun datar (1/2): "))

if pilih == 1:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print("Luas Persegi Panjang adalah:", luas)

elif pilih == 2:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas Segitiga adalah:", luas)

else:
    print("Pilihan tidak tersedia!")
