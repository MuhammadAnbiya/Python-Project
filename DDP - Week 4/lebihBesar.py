# Tuliskan program yang meminta input dua bilangan dan menampilkan bilangan yang lebih besar.

a = float(input("bilangan pertama : "))
b = float(input("bilangan kedua : "))

if a > b:
    print("bilangan pertama lebih besar dari bilangan kedua")
elif a < b:
    print("bilangan kedua lebih besar dari bilangan pertama")
else:
    print("bilangan pertama dan kedua nilainya sama")