# Buatlah program yang menghitung luas dan keliling segitiga berdasarkan panjang sisi-sisinya. 
# (Gunakan Rumus Heron)


a = float(input("masukan panjang sisi pertama : "))
b = float(input("masukan panjang sisi kedua : "))
c = float(input("masukan panjang sisi ketiga : "))

s = (a + b + c) / 2

luas = (s*(s-a)*(s-b)*(s-c))**0.5

print(f"luas dari segitiga heron tersebut adalah {luas} cm^2")