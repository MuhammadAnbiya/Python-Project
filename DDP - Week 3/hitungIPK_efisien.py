# Buatlah Perhitungan IPK untuk semester ini berdasarkan nilai yang di input
# Mata kuliah semster ini adalah Algoritma, Perancangan Objek, Kalkulus, Etika Profesi, Databases, dan Englis 1

algoritma = float(input("masukan nilai algoritma anda : "))
SKSalgoritma = int(input("masukan sks algoritma anda : "))
perancanganObjek = float(input("masukan nilai perancangan objek anda : "))
SKSperancanganObjek = int(input("masukan sks perancangan objek anda : "))
kalkulus = float(input("masukan nilai kalkulus anda : "))
SKSkalkulus = int(input("masukan sks kalkulus anda : "))
etikaProfesi = float(input("masukan nilai etika profesi anda : "))
SKSetikaProfesi = int(input("masukan sks etika profesi anda : "))
dataBases = float(input("masukan nilai data bases anda : "))
SKSdataBases = int(input("masukan sks data bases anda : "))
englis1 = float(input("masukan nilai englis 1 anda : "))
SKSenglis1 = int(input("masukan sks englis 1 anda : "))

def hitungTotal (nilai, sks):
    if nilai < 30:
        return 0 * sks 
    else:
        if nilai > 100:
            return 4 * sks
        else:
            bobot = 1
            for x in range(35,101, +5):
                if nilai < x:
                    return bobot * sks
                else:
                    bobot = bobot +  0.25
                
                
totalAlgoritma = hitungTotal(algoritma, SKSalgoritma)
totalPerancanganObjek = hitungTotal(perancanganObjek, SKSperancanganObjek)
totalKalkulus = hitungTotal(kalkulus, SKSkalkulus)
totalEtikaProfesi = hitungTotal(etikaProfesi, SKSetikaProfesi)
totalDataBases = hitungTotal(dataBases, SKSdataBases) 
totalEnglis1 = hitungTotal(englis1, SKSenglis1)
totalSKS = SKSalgoritma + SKSperancanganObjek + SKSkalkulus + SKSetikaProfesi + SKSdataBases + SKSenglis1

IPK = (totalAlgoritma + totalPerancanganObjek + totalKalkulus + totalEtikaProfesi + totalDataBases + totalEnglis1) / totalSKS
print(f"jadi total IPK anda adalah {IPK:.2f}")