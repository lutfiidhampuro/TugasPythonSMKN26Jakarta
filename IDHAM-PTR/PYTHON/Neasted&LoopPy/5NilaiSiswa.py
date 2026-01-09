data_siswa = [
    ["Andi", 80, 75, 85, 90, 88],
    ["Budi", 70, 65, 75, 80, 78],
    ["Citra", 90, 85, 88, 92, 95],
    ["Dewi", 60, 70, 65, 75, 68],
    ["Eko", 85, 80, 82, 88, 90]
]

print("Nama\t\tMTK\tBING\tBINDO\tAgama\tKejuruan\tRata-Rata")
print("-" * 70)

for siswa in data_siswa:
    nama = siswa[0]
    nilai = siswa[1:]
    rata = sum(nilai) / len(nilai)
    print(f"{nama:<10}\t", end="")

    for n in nilai:
        print(f"{n}\t", end="")
    
    print(f"{rata:.2f}")
