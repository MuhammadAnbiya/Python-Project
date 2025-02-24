# Tuliskan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih besar, 
# 2 bilangan lebih besar dari yang lain atau semua bilangan sama besar

a = float(input("bilangan pertama : "))
b = float(input("bilangan kedua : "))
c = float(input("bilangan ketiga : "))


if a == b == c:
    print("semua bilangan sama besar")
elif a == b:
    if a > c:
        print(f"bilangan pertama dan kedua sama sama {a} dan lebih besar dari bilangan ketiga yaitu {c}")
    else:
        print(f"bilangan pertama dan kedua sama sama {a} dan lebih kecil dari bilangan ketiga yaitu {c}")

elif a == c:
    if a > b:
        print(f"bilangan pertama dan ketiga sama sama {a} dan lebih besar dari bilangan kedua yaitu {b}")
    else:
        print(f"bilangan pertama dan ketiga sama sama {a} dan lebih kecil dari bilangan kedua yaitu {b}")

elif b == c:
    if b > a:
        print(f"bilangan kedua dan ketiga sama sama {b} dan lebih besar dari bilangan pertama yaitu {a}")
    else:
        print(f"bilangan kedua dan ketiga sama sama {b} dan lebih kecil dari bilangan pertama yaitu {a}")
elif a > b and a > c:
    print("angka yang paling besar adalah bilangan pertama")
elif b > c and b > a:
    print("angka yang paling besar adalah bilangan kedua")
elif c > a and c > b:
    print("angka yang paling besar adalah bilangan ketiga")