# Buatlah form pendaftaran untuk masuk universitas
# Nama, Tempat lahir, Tanggal Lahir, Tahun lahir, 3 Nilai Mata Pelajaran (English, Mtk, Indonesia), Jenis Kelamin

# Dia akan disarankan ke
# Jurusan Teknik Informatika jika rata-rata nilainya >=80 dan jenis kelaminnya laki-laki
# Jurusan Sistem Informasi jika rata-rata nilainya >=80 dan jenis kelamin Perempuan
# Selebihnya disarankan masuk jurusan DKV

# Meskipun demikian, Mahasiswa yang diterima hanya yang dibawah umur 25


print("===================================================================")
print("             FORM PENDAFTARAN UNIVERSITAS NUSA PUTRA               ")
print("===================================================================")
nama = input("Masukan nama lengkap anda : ")
umur = int(input("Masukan umur anda : "))
tempatLahir = input("Masukan tempat lahir anda : ")
tanggalLahir = int(input("Masukan tanggal lahir anda : "))
tahunLahir = int(input("Masukan tahun lahir anda : "))
jenisKelamin = input("Masukan jenis kelamin anda (lakilaki / perempuan) : ")

print("===================================================================")
print(" SELANJUTNYA MASUKAN NILAI MATA PELAJARAN (English, MTK, Indonesia) ")
print("===================================================================")

english = float(input("Masukan nilai dari mata pelajaran english anda : "))
mtk = float(input("Masukan nilai dari mata pelajaran MTK anda : "))
indonesia = float(input("Masukan nilai dari mata pelajaran indonesia anda :"))

if umur >= 25:
    print("Umur anda sudah tidak memenuhi syarat untuk mendaftar")
elif (english+mtk+indonesia)/3 >= 80 and jenisKelamin == "lakilaki":
    print("Anda disarankan untuk masuk Jurusan Teknik Informatika")
elif (english+mtk+indonesia)/3 >= 80 and jenisKelamin == "perempuan":
    print("Anda disarankan untuk masuk Jurusan Sistem Informasi")
else:
    print("Anda disarankan untuk masuk Jurusan DKV")


    


