# Tulisan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih kecil

a = (float(input("masukan bilangan pertama  : ")))
b = (float(input("masukan bilangan kedua  : ")))
c = (float(input("masukan bilangan ketiga  : ")))


if a < b and a < c:
    print("angka yang paling kecil adalah bilangan pertama")
elif b < c and b < a:
    print("angka yang paling kecil adalah bilangan kedua")
elif c < a and c < b:
    print("angka yang paling kecil adalah bilangan ketiga")
else:
    print("bilangan tidak boleh sama")
    

    