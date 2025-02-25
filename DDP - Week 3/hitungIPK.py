# Buatlah Perhitungan IPK untuk semester ini berdasarkan nilai yang di input
# Mata kuliah semster ini adalah Algoritma, Perancangan Objek, Kalkulus, Etika Profesi, Databases, dan Englis 1

nilaiAlgoritma = float(input("masukan nilai anda : "))
if nilaiAlgoritma <30:
    indeksAlgoritma = "E"
elif nilaiAlgoritma >= 30 and nilaiAlgoritma < 50:
    indeksALgoritma = "D"
elif nilaiAlgoritma >= 50 and nilaiAlgoritma < 70:
    indeksALgoritma = "C"
elif nilaiAlgoritma >= 70 and nilaiAlgoritma < 90 :
    indeksAlgoritma = "B"
else:
    indeksAlgoritma = "A"
    
if indeksAlgoritma:
    print("A")

perancanganObjek = float(input("masukan nilai anda : "))
etikaProfesi = float(input("masukan nilai anda : "))
dataBases = float(input("masukan nilai anda : "))
englis1 = float(input("masukan nilai anda : "))

IP = (nilaiAlgoritma + perancanganObjek + etikaProfesi + dataBases + englis1) / 5

if IP < 50:
    indeks = "E"
elif IP <= 60:
    indeks = "D"
elif IP <= 70:
    indeks = "C"
elif IP <= 80:
    indeks = "B"
else:
    indeks = "A"

if indeks == "A":
    print("A")
    if IP < 50:
    indeks = "E"
elif IP <= 60:
    indeks = "D"
elif IP <= 70:
    indeks = "C"
elif IP <= 80:
    indeks = "B"
else:
    indeks = "A"

if IP < 50:
    indeks = "E"
elif IP <= 60:
    indeks = "D"
elif IP <= 70:
    indeks = "C"
elif IP <= 80:
    indeks = "B"
else:
    indeks = "A"

if IP < 50:
    indeks = "E"
elif IP <= 60:
    indeks = "D"
elif IP <= 70:
    indeks = "C"
elif IP <= 80:
    indeks = "B"
else:
    indeks = "A"

if IP < 50:
    indeks = "E"
elif IP <= 60:
    indeks = "D"
elif IP <= 70:
    indeks = "C"
elif IP <= 80:
    indeks = "B"
else:
    indeks = "A"

