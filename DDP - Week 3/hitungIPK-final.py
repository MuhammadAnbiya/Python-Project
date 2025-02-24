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
    if nilai <30:
        return 0 * sks
    elif nilai <= 34:
        return 1 * sks
    elif nilai <= 39:
        return  1.25 * sks
    elif nilai <= 44:
        return 1.5 * sks
    elif nilai <= 49:
        return 1.75 * sks
    elif nilai <= 54:
        return 2 * sks
    elif nilai <= 59:
        return 2.25 * sks
    elif nilai <= 64:
        return 2.5 * sks
    elif nilai <= 69:
        return 2.75 * sks
    elif nilai <= 74:
        return 3 * sks
    elif nilai <= 79:
        return 3.25 * sks
    elif nilai <= 84:                      
        return 3.5 * sks
    elif nilai <= 89:
        return 3.75 * sks
    else:
        return 4 * sks
    

totalAlgoritma = hitungTotal(algoritma, SKSalgoritma)
totalPerancanganObjek = hitungTotal(perancanganObjek, SKSperancanganObjek)
totalKalkulus = hitungTotal(kalkulus, SKSkalkulus)
totalEtikaProfesi = hitungTotal(etikaProfesi, SKSetikaProfesi)
totalDataBases = hitungTotal(dataBases, SKSdataBases) 
totalEnglis1 = hitungTotal(englis1, SKSenglis1)
totalSKS = SKSalgoritma + SKSperancanganObjek + SKSkalkulus + SKSetikaProfesi + SKSdataBases + SKSenglis1

IPK = (totalAlgoritma + totalPerancanganObjek + totalKalkulus + totalEtikaProfesi + totalDataBases + totalEnglis1) / totalSKS
print(f"jadi total IPK anda adalah {IPK:.2f}")