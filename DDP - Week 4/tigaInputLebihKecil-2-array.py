arr = []

arr.append(float(input("masukan bilangan pertama  : ")))
arr.append(float(input("masukan bilangan kedua  : ")))
arr.append(float(input("masukan bilangan ketiga  : ")))

arrayUrut = sorted(arr)
print("bilangan yang paling kecil adalah "+ str(arrayUrut[0]))  