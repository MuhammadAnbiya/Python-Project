# Dina memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang kurang dari 10 dan lebih dari 100, dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Implementasikan ini dengan menggunakan metode-metode yang tepat dari list.

# Input: [105, 20, 8, 150, 30, 5, 200]
# Output: [20, 30]

Input = [105, 20, 8, 150, 30, 5, 200]

for i in Input[:]:
    if i < 10 or i > 100:
        Input.remove(i)
        
print(sorted(Input))