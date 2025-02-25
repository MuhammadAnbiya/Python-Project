#Membuat Angka Fibonachi

panjang = int(input("Masukan panjang Fibonachi yang anda inginkan : "))

k1 = 1
k2 = 1
for i in range(1, panjang + 1):
     if i < 3:
        print(1, end= " ")
     else:
        k3 = k1 + k2
        print(k3, end=" ")
        k1 = k2
        k2 = k3