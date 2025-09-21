namaAnda = input("Masukkan Nama Anda: ")
DaftarUsia = (17, 18, 19, 20)

if namaAnda == "Idham" or namaAnda == "Lutfi":
  print("Usia anda adalah:", DaftarUsia[0])
elif namaAnda == "Aldi" or namaAnda == "aldi":
  print("Usia anda adalah:", DaftarUsia[1])
elif namaAnda == "Rizki" or namaAnda == "rizki":
  print("Usia anda adalah:", DaftarUsia[2])
elif namaAnda == "Purwanto" or namaAnda == "purwanto":
  print("Usia anda adalah:", DaftarUsia[3])
else:
  print("Nama Anda Tidak Ditemukan")
print("Terima Kasih")
exit()
