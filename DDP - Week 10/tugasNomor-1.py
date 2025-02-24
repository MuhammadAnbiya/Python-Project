# Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method.

# Input: [8, 3, 12, 4, 7, 2]
# Output: [12, 8, 7, 4, 0, 0]

def inputAngka():
    angka = []
    
    while True:
        number = input('Masukan angka atau tulis "selesai" jika sudah : ')
        if number.lower() == 'selesai':
            break
    
        try:
            angka.append(int(number))
        except ValueError:
            print("Masukkan angka yang valid.")
    return angka

arr = inputAngka()

for i in range(len(arr)):
    if arr[i] < 5:
        arr[i] = 0  
        
arr.sort(reverse=True)
print(f"Output : {arr}")




    
    
    
    
