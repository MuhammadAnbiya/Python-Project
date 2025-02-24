# Jumlah 4 buah bilangan kuadrat pertama adalah 30 (30=1+4+9+16), 
# berapakah jumlah 1000 bilangan kuadrat pertama?

jumlah = int(input('Masukan Berapa Digit Bilangan Kuadrat : '))
hasil = 0

for i in range(1, jumlah + 1):
    kuadrat = (i**2) 
    hasil = hasil + kuadrat

print("Jadi jumlah %i bilangan kuadrat pertama adalah %i"%(jumlah, hasil))
