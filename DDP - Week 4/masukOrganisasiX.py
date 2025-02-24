# Buatlah program untuk menghitung kelayakan orang lulus organisasi X. Organisasi X memiliki kriteria untuk Anggota
# 1. Perempuan dengan berat badan minimal 45kilo gram, maks 50 kilogram dan Tingginya minimal 165 cm dan 
#     Usianya kurang dari 20 tahun
# 2. Laki-laki dengan berat badan maks 70 kilo dan Tingginya minimal 170 cm dan usianya maks 25 tahun
# 3. Laki-laki dan Perempuan dengan nilai rata-rata Akademis 90 dan usianya kurang dari 30 tahun
# 4. Laki-laki dan Perempuan yang Memiliki Skill Menembak, Memanah atau Berkuda

# Ke 4 Kriteria diatas akan diterima hanya dan hanya jika tidak memiliki anggota tubuh yang cacat.

# berat badan, tinggi badan, usia, jenis kelamin, nilai rata rata, skill, tidak cacat.

print("===================================================================")
print("                FORM PENDAFTARAN MASUK ORGANISASI X                ")
print("===================================================================")
jenisKelamin = input("Masukan jenis kelamin anda (lakilaki / perempuan) : ")
usia = int(input("Masukan usia anda sekarang : "))
tinggiBadan = float(input("Masukan tinggi badan anda : "))
beratBadan = float(input("Masukan berat badan anda : "))
nilai = float(input("Masukan nilai rata rata anda : "))
disabilitas = input("Apakah anda penyandang disabilitas ? (ya / tidak) : ")
print("===================================================================")
print("    BERITAHU KAMI TENTANG SKILL YANG ANDA MILIKI (MIN. 3 SKILL)    ")
print("===================================================================")
skill1 = input("1. ")  #[evaluasi pak nunu] : lebih bagus untuk dibuat pertanyaan ya atau tidak
skill2 = input("2. ")  
skill3 = input("3. ")

if disabilitas == "ya":
    print("Maaf, kamu tidak memenuhi kriteria")
elif((jenisKelamin == "perempuan") and (beratBadan >= 45 and beratBadan <= 50) and (tinggiBadan >= 165) and (usia < 20)):
    print("Selamat! kamu memenuhi kriteria untuk masuk Organisasi X")
elif ((jenisKelamin == "lakilaki") and (beratBadan <= 70) and (tinggiBadan >= 170) and (usia <= 25)):
    print("Selamat! kamu memenuhi kriteria untuk masuk Organisasi X")
elif ((jenisKelamin == "lakilaki" or jenisKelamin == "perempuan") and (nilai >= 90) and (usia <= 30)):
    print("Selamat! kamu memenuhi kriteria untuk masuk Organisasi X")
elif ((jenisKelamin == "lakilaki" or jenisKelamin == "perempuan") and 
      ((skill1 == "menembak" or skill1 == "memanah" or skill1 == "berkuda")
      or (skill2 == "menembak" or skill2 == "memanah" or skill2 == "berkuda") 
      or (skill3 == "menembak" or skill2 == "memanah" or skill3 == "berkuda"))):
    print("Selamat! kamu memenuhi kriteria untuk masuk Organisasi X")
else:
    print("Maaf, kamu tidak memenuhi kriteria")




