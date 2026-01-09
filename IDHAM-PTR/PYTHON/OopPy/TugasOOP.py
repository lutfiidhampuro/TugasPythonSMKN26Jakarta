# Class Barang
class Barang:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def total_harga(self):
        return self.harga * self.jumlah


# Class Kasir
class Kasir:
    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)

    def hitung_total(self):
        total = 0
        for barang in self.daftar_barang:
            total += barang.total_harga()
        return total

    def tampilkan_struk(self):
        print("\n===== STRUK BELANJA =====")
        for barang in self.daftar_barang:
            print(f"{barang.nama} x{barang.jumlah} = Rp{barang.total_harga()}")
        print("-------------------------")
        print(f"TOTAL BAYAR : Rp{self.hitung_total()}")
        print("=========================")


# Program Utama (CLI)
kasir = Kasir()

while True:
    nama = input("Nama barang (ketik 'selesai' untuk stop): ")
    if nama.lower() == "selesai":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    barang = Barang(nama, harga, jumlah)
    kasir.tambah_barang(barang)

kasir.tampilkan_struk()
