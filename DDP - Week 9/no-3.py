# Array: [1, 2, 3, 2, 4, 3, 5]
# Output: Array setelah menghapus angka 2 dan mengurutkannya secara terbalik adalah [5, 4, 3, 3, 1]

arr = [1, 2, 3, 2, 4, 3, 5]
arr_hasil = []


for i in arr:
    if i != 2:
        arr_hasil.append(i)
        
arr_hasil.sort(reverse= True)
print(arr_hasil)