def rata2 (nilai):
  total = sum(nilai)
  jumlah = len(nilai)
  rata2 = total / jumlah 
  return round(rata2,2)

nilai1 = int(input("Masukkan Nilai TUGAS : "))
nilai2 = int(input("Masukkan Nilai PTS : "))
nilai3 = int(input("Masukkan Nilai UAS : "))

rata = rata2( nilai = [nilai1, nilai2, nilai3] )
print("Nilai :" , nilai1, nilai2, nilai3)
print("Rata-rata : ", rata)


