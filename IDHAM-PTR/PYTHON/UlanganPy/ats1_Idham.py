nilai_siswa = ["Yardhan Zhafran Reyfhanza", "X SIJA 2", 95, 83, 73, 85, 70]

nama = nilai_siswa[0]
kelas = nilai_siswa[1]
nilai = nilai_siswa[2]

n1 = nilai_siswa[2]
n2 = nilai_siswa[3]
n3 = nilai_siswa[4]
n4 = nilai_siswa[5]
n5 = nilai_siswa[6]

sangat_baik = 0
baik = 0
cukup = 0

print(f"Nama Siswa : {nama}")
print(f"Kelas Siswa : {kelas}")
print(f"Daftar Nilai dan Keterangan :")

if 90 <= n1 <= 100:
    print(f"Nilai {n1} → Sangat Baik")
    sangat_baik += 1
elif 80 <= n1 <= 89:
    print(f"Nilai {n1} → Baik")
    baik += 1
else:
    print(f"Nilai {n1} → Cukup")
    cukup += 1

if 90 <= n2 <= 100:  
    print(f"Nilai {n2} → Sangat Baik")
    sangat_baik += 1
elif 80 <= n2 <= 89:
    print(f"Nilai {n2} → Baik")
    baik += 1
else:
    print(f"Nilai {n2} → Cukup")
    cukup += 1

if 90 <= n3 <= 100:
    print(f"Nilai {n3} → Sangat Baik")
    sangat_baik += 1
elif 80 <= n3 <= 89:
    print(f"Nilai {n3} → Baik")
    baik += 1
else:
    print(f"Nilai {n3} → Cukup")
    cukup += 1

if 90 <= n4 <= 100:
    print(f"Nilai {n4} → Sangat Baik")
    sangat_baik += 1
elif 80 <= n4 <= 89:
    print(f"Nilai {n4} → Baik")
    baik += 1
else:
    print(f"Nilai {n4} → Cukup")
    cukup += 1

if 90 <= n5 <= 100:
    print(f"Nilai {n5} → Sangat Baik")
    sangat_baik += 1
elif 80 <= n5 <= 89:
    print(f"Nilai {n5} → Baik")
    baik += 1
else:
    print(f"Nilai {n5} → Cukup")
    cukup += 1


print("\n-----Rekapitulasi-----")
print(f"Jumlah Nilai Sangat Baik: {sangat_baik}")
print(f"Jumlah Nilai Baik: {baik}")
print(f"Jumlah Nilai Cukup: {cukup}")