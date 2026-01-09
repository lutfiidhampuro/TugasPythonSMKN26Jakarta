while True:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    if angka == 0:
        print("Program berhenti.")
        break
    elif angka < 0:
        print("Masukkan angka positif!")
        continue
    else:
        print(f"Anda memasukkan angka: {angka}")
