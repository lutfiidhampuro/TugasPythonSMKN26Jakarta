def ganjilgenap(n):
    if n % 2 == 0:
        return "Genap"
    else:
        return "Ganjil" 

while True:
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan < 0:
        print("Bilangan harus positif, Tolong coba lagi")
    elif bilangan == 0:
        print("Bilangan nol bukan ganjil atau genap")
        print("Program selesai, Terima kasih")
        exit()
    else : 
        hasil = ganjilgenap(bilangan)
        print(f"Bilangan {bilangan} adalah {hasil}")

