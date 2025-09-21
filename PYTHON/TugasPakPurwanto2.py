phi_input = input("Masukkan nilai phi (misal 3.14 atau 22/7): ")
if phi_input == "22/7":
    phi = 22/7
elif phi_input == "3.14":
    phi = 3.14
else:
    print("Input phi tidak valid, gunakan 3.14 atau 22/7")
    exit()
r = float(input("Masukkan jari-jari lingkaran: "))
luas = phi * r * r
print(f"Luas lingkaran adalah: {luas}")

