# buatlah kode pemrograman yang bisa mengecek sebuah bilangan adalah bilangan ganjil atau genap
# dengan tipe data integer dan float

angka = float(input("Masukan angka yang ingin di uji coba? "))

if angka % 2 == 0:
    x = int(angka)
    print(str(x) + " Adalah bilangan Genap")
    
elif angka % 2 == 1:
    x = int(angka)
    print(str(x) + " Adalah bilangan Ganjil")

else:
    print(str(angka) + " Adalah bilangan desimal")