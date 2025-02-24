matrikA = []
matrikB = []

for i in range(2):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukkan elemen [{i+1}, {j+1}] untuk Matriks 1: "))
        baris.append(nilai)
    matrikA.append(baris)  

for i in range(2):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukkan elemen [{i+1}, {j+1}] untuk Matriks 2: "))
        baris.append(nilai)
    matrikB.append(baris)  

result = []
for i in range(2):
    baris = []
    for j in range(3):
        baris.append(matrikA[i][j] + matrikB[i][j])  
    result.append(baris)  

for baris in result:
    print(baris)

print("\nMatriks A:", matrikA)
print("Matriks B:", matrikB)
