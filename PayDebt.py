# buatlah sistem deposit dan bayar hutang yang output nya bisa menjelaskan apakah
# uang dari si pengisi cukup untuk membayar utang atau tidak

nama = input("Masukan nama anda : ")
keterangan = input("Masukan status anda : ")
saldo_awal = int(input("Masukan total saldo awal anda : "))

deposit = int(input("Berapa jumlah yang akan anda deposit : "))
saldo_total = saldo_awal + deposit

hutang = int(input("Berapa hutang yang anda miliki : "))

if saldo_total >=  hutang:
    print("Anda bisa membayar hutang anda dengan sisa saldo Rp. " + str(saldo_total - hutang))

elif saldo_total < hutang:
    print(("Maaf total uang anda " + str(saldo_total)) + " dan tidak cukup untuk membayar hutang")

else:
    print("Saldo anda tersisa " + str(saldo_total) + " Anda bisa membayar hutang tetapi uang anda akan habis")