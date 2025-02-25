# Tuliskan program untuk menentukan bilangan itu bilangan (ganjil/genap) positif, negatif atau 0

a = float(input("masukan bilangan : "))

if a % 2 == 0:
    if a > 0:
        print(f"{a} adalah bilangan genap positif")
    elif a < 0:
        print(f"{a} adalah bilangan genap negatif")
    else:
        print(f"{a} adalah bilangan genap sama dengan nol")
else:
    if a > 0:
        print(f"{a} adalah bilangan ganjil positif")
    elif a < 0:
        print(f"{a} adalah bilangan ganjil negatif")
    else:
        print(f"{a} adalah bilangan sama dengan nol")