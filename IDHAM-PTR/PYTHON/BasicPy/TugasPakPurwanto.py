# Input Nama
nama = input("Masukkan nama Anda: ")

# Input Kelas
kelas = input("Masukkan kelas Anda: ")

#Input Sekolah
sekolah = input("Masukkan nama sekolah Anda: ")

# Input jenis kelamin
jenis_kelamin = input("Masukkan jenis kelamin (Laki-Laki/Perempuan): ")

if jenis_kelamin == "Laki-Laki":
    print("Anda adalah Laki-laki")
else:
    print("Anda adalah Perempuan")

# Input umur
Umur = int(input("Masukkan umur Anda: "))
if Umur <= 18:
    print("Anda masih di bawah umur")
elif Umur <= 60:
    print("Anda sudah dewasa")
elif Umur <= 100:
    print("Anda sudah tua")

print("\n-----Data Anda-----")
print(f"Nama Anda: {nama}")
print(f"Kelas Anda: {kelas}")
print(f"Nama Sekolah Anda: {sekolah}")
print(f"Jenis Kelamin: {jenis_kelamin}")
print(f"Umur Anda: {Umur} tahun")