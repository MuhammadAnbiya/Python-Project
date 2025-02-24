# Array: [1, 2, 3, 2, 4, 3, 5]
# Output: Array setelah menghapus duplikat adalah [1, 2, 3, 4, 5]

arr =  [1, 2, 3, 2, 4, 3, 5]
arr_hasil = []

for element in arr:
    if element not in arr_hasil:
        arr_hasil.append(element)        
print(arr_hasil)