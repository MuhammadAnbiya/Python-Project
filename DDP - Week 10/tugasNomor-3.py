# Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis. Bantulah Rani untuk mencapai ini.

# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']


kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
sortir = []

for i in kata:
    if len(i) >= 5:
        sortir.append(i)

print(sorted(sortir))