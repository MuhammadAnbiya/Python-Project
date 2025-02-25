# Buatlah konversi nilai dengan kriteria

# <50 E
# 50-60 D
# 60-70 C
# 70-80 D
# selebihnya A


nilai = float(input("masukan nilai anda selama semester ini : "))

if nilai < 50:
    indeks = "E"
elif nilai < 60:
    indeks = "D"
elif nilai < 70:
    indeks = "C"
elif nilai < 80:
    indeks = "B"
else:
    indeks = "A"
    
print(f"nilai anda pada semester ini adalah {indeks}")