BangunDatar = str(input("Masukkan Nama Bangun Datar: "))
if BangunDatar == "Persegi" or BangunDatar == "persegi":
    Sisi = int(input("Masukkan Sisi: "))
    Luas = Sisi * Sisi
    print("Luas Persegi adalah:", Luas)
elif BangunDatar == "Persegi Panjang" or BangunDatar == "persegi panjang":
    Panjang = int(input("Masukkan Panjang: "))
    Lebar = int(input("Masukkan Lebar: "))
    Luas = Panjang * Lebar
    print("Luas Persegi Panjang adalah:", Luas) 
elif BangunDatar == "Segitiga":
    Alas = int(input("Masukkan Alas: "))
    Tinggi = int(input("Masukkan Tinggi: "))
    Luas = 0.5 * Alas * Tinggi
    print("Luas Segitiga adalah:", Luas)
elif BangunDatar == "Lingkaran" or BangunDatar == "lingkaran":
    phi_input = input("Masukkan nilai phi (misal 3.14 atau 22/7): ")
    if phi_input == "22/7":
        phi = 22/7
    elif phi_input == "3.14":
        phi = 3.14
    else:
        print("Input phi tidak valid, gunakan 3.14 atau 22/7")
        exit()
    r = float(input("Masukkan jari-jari lingkaran: "))
    Luas = phi * r * r
    print(f"Luas Lingkaran adalah: {Luas}")
else:
    print("Bangun Datar Tidak Tersedia")