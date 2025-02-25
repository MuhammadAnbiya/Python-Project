# # Buatlah kode pemrograman yang bisa mengurutkan angka dari terbesar ke terkecil, lalu berapa hasil nya jika semua 
# # angka di tambahkan dan tentukan rata ratanya (minimal 12 angka).

r = []
for x in range(1,13):
        user_input = (input(f"Masukan angka ke-{x} : "))
        r.append(float(user_input))

angka_urut = sorted(r)
print("Urutan angka dari yang terkecil sampai terbesar dari himpunan bilangan tersebut adalah : \n" + str(angka_urut))

hasil_semua = sum(angka_urut)
print("Jadi Total seluruh angka dari himpunan bilangan tersebut adalah : \n" + str(hasil_semua))

rata_rata = hasil_semua / len(angka_urut)
print("Jadi rata rata dari himpunan bilangan tersebut adalah : \n" + str(rata_rata))