#Diskon di Indomaret
belanja = float(input("Masukan total belanjaan anda : "))
keterangan = ""

if belanja > 60_000:
    diskon = belanja * 10/100
    total = belanja - diskon
    keterangan = " Anda mendapatkan diskon sebesar 10% karena belanja lebih dari 60 ribu" 
else: 
    total = belanja
    keterangan = " Anda tidak mendapatkan diskon apapun, belanja diatas 60 ribu baru dapatkan diskonya"

print("total belanjaan anda adalah %i rupiah"%total + keterangan)   