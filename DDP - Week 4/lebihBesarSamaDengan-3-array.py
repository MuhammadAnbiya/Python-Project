arr = []

a = float(input("bilangan pertama : "))
b = float(input("bilangan kedua : "))
c = float(input("bilangan ketiga : "))

arr.append(a)
arr.append(b)
arr.append(c)

arrayUrut = sorted(arr)


if a == b == c:
    print("semua bilangan sama besar")
elif a == b:
    if a > c:
        print(f"bilangan pertama dan kedua sama sama {a} dan lebih besar dari bilangan pertama yaitu {c}")
    else:
        print(f"bilangan pertama dan kedua sama sama {a} dan lebih kecil dari bilangan pertama yaitu {c}")

elif a == c:
    if a > b:
        print(f"bilangan pertama dan ketiga sama sama {a} dan lebih besar dari bilangan kedua yaitu {b}")
    else:
        print(f"bilangan pertama dan ketiga sama sama {a} dan lebih kecil dari bilangan kedua yaitu {b}")

elif b == c:
    if b > a:
        print(f"bilangan kedua dan ketiga sama smaa {b} dan lebih besar dari bilangan ketiga yaitu {a}")
    else:
        print(f"bilangan kedua dan ketiga sama smaa {b} dan lebih kecil dari bilangan ketiga yaitu {a}")
else: 
    print("bilangan yang paling besar adalah "+ str(arrayUrut[2]))