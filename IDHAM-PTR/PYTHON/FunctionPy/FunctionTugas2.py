def luasPersegiPanjang(p, l):
  luas = p * l
  return luas

def KelilingPersegiPanjang(p, l):
  keliling = 2 * (p + l)
  return keliling

panjang = int(input("Masukkan Panjang : "))
lebar = int(input("Masukkan Lebar : "))
luas = luasPersegiPanjang(panjang, lebar)
keliling = KelilingPersegiPanjang(panjang, lebar)
print("Luas Persegi Panjang : ", luas)
print("Keliling Persegi Panjang : ", keliling)