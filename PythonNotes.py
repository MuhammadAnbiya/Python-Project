# >> Python dikembangkan oleh Guido van Rossum, Programmer asal Belanda tahun 1991 di CWI,Amsterdam
# >> Python adalah bahasa lanjutan dari bahasa pemrograman ABC
# >> Nama Python diambil dari acara televisi kesukaan Guido yaitu Monty Python's flying Circus
# >> IDLE ( Integrated Development and Learning Environment)
#
#
# print("Hello World!")
# output = Hello World!
#
# >> Python adalah bahasa pemrograman yang bersifat case sensitive artinya beda satu huruf berpengaruh terhadap kode
# >> Identation adalah penataan baris baris kode yang menjorok kedalam
# >>>>> Type data dalam python
# string = str
# number = (integer, Float, Complex Number)
# Boolean = True / False
# list = [a, b, c]
# tuple = (a, b, b)
# set = {a, b, c}
# dictionary = {a, b, c}
# >>>>> Reserved Word Python ( kata kata yang sudah menjadi syntax dalam python)
#
# print("Selamat Datang!")
# nama = input("Silahkan masukan nama anda : ")
# print("Hallo ", nama)
#
# angka = 123
# SMA = "Sekolah Menengah Atas"
# pertambahan = angka + 100
# kepanjangan = "Kepanjangan dari SMA adalah"
# print("Hasil dari 123 + 100 adalah = ", pertambahan)
# print(kepanjangan, SMA)
# output = Hasil dari 123 + 100 adalah =  223
#          Kepanjangan dari SMA adalah Sekolah Menengah Atas
#
# >>>>> Assigment (proses memasukan data kedalam variabel)
#
# a = 1
# print(a)
# a = a + 1
# print(a)
# a = a * 2
# print(a)
#
# >>>>> Multiple Assignment (proses memasukan beberapa nilai kedalam beberapa variabel sekaligus)
# a = b = c = 10
# print(a, b, c)
# output = 10 10 10
#
# a, b, c = 10, 20, "seratus"
# print(a, b, c)
# output = 10 20 seratus
#
# >>>>> loosely Type Language sebuah bahasa pemrograman yang variabel nya tidak terikat pada sebuah tipe tertentu
# usia = 10
# print(usia)
# output = 10
#
# usia = "sepuluh"
# print(usia)  >>> yang tadinya usia outputnya 10, jadi usia outputnya "sepuluh"
# outputnya = sepuluh
#
# >>>>> Swap Variabel
# x = 10
# y = 20
# print(x, y)
# output = 10 20
# x, y = y, x
# print(x, y)
# output = 20 10
#
# >>>>> Penulisan string
#    1. menggunakan kutip satu ('') atau kutip dua ("")
#    2. menggunakan kutip tiga ('''  ''')
#    3. menggunakan Raw String
#        ex :
# print("Hello\nWorld")
# output = Hello
#          World
# print(r"Hello\nWorld")
# output = Hello\nWorld
# print(''' aku
#         adalah seorang
#         web dev''')
# output =  aku
#         adalah seorang
#         web dev
#
# >>>>> escape character
# \'  = tanda kutip tunggal
# \" = tanda kutip ganda
# \t = tab
# \n = baris baru
# \\ = garis miring
#
# print("\' she\'s mine\t but \n gatau nulis apa\\\'")
# output = ' she's mine	 but
#           gatau nulis apa\'
#
# >>>>> escape code (tulisan berwarna)
# ex = \033 digunakan untuk menampilkan tesk string dalam warna
# print("\033[1;32;40m Tulisan ini berwarna lho ... \n")
# \033 digunakan untuk menampilkan ANSI Code di mana
# 1 adalah style teks
# 32 adalah warna teks (hijau)
# 40 adalah warna latar belakang (hitam)
#
# >>>>> print tanpa membuat garis baru (end)
# print("Hallo dunia", end='')
# print("Aku mau jadi software developer")
# output = Hallo duniaAku mau jadi software developer
#
#
# >>>>> menggunakan.format
#
# print("Hallo {0} apa kabar!" .format("Edi"))
# # output = Hallo Edi apa kabar!
# print("Usia saya {0} tahun lebih muda dari kaka saya dan usia kaka saya {1} tahun" .format(10, 35))
# output = Usia saya 10 tahun lebih muda dari kaka saya dan usia kaka saya 35 tahun
# angka 0,1,2 dst menunjukan index
#
# >>>>> bekerja dengan number
#
# integer (int) = tipe bilangan bulat (1, 2, 100, 1500 dst.)
# float (float) = tipe bilangan pecahan atau desimal (0.0002, 900.99)
# complex numbers = tipe bilangan kompleks atau bilangan imajiner (bilangan yang memiliki tanda negatif di bawah tanda akar )
#                   (10j, 5j, 1j) >> pada python huruf j digunakan untuk menunjukan angka akar kuadrat dari -1
#                   jadi, 10j artinya 10 akar -1
#
# base 2 = menghasilkan angka 0 dan 1 saja (binary)
# base 8 = menggunakan angka dari 0 sampai 7 (oct)
# base 10 = angka bulat biasa
# base 16 = menggunakan angka dari 0 sampai 9 bersamaan dari huruf A sampai F (hexadesimal)
#
# print(0b10)    #>> Base2 bin()
# output = 2
# print(0o100)   #>> Base8 oct()
# output = 64
# print(0x1000)  #>> Base16 hex()
# output = 4096
#
# angka_base = 0b100
# print("100 Binary :", angka_base)
# output = 100 Binary : 4
#
#
# >>>>> Menggunaka bilangan pecahan (Floating)
#
# scientific notation = 2.55e2 >> huruf e memisahkan angka yang ada dikirinya dengan pangkat yang ada dikanan nya
# 2.55e2 artiya 2.55 pangkat 2
# 2.55e-2 artinya 2.55 pangakt -2
#
# >>>>> Mengubah string menjadi number dan sebaliknya
#
# huruf_a = ord("a")
# print("Huruf a diwakili oleh angka : ", huruf_a)
# # output = Huruf a diwakili oleh angka :  97
# angka = int("25")
# print("75 + 25 = " , 75 + angka)
# # output = 75 + 25 =  100
# teks = str(25)
# print("Variabel teks bertipe data ", type(teks))
# # output = Variabel teks bertipe data  <class 'int'>
#
# type() = (berfungsi untuk menampilkan tipe data)
# ord() = (berfungsi untuk menghasilkan sebuah nilai integer berupa kode ASCII dari sebuah karakter.)

# >>>>> Mengenal Operand dan Operator
# >> Operand = nilai asal yang akan diolah
# >> Operator = Intruksi untuk mendapatkan hasil olahan
# ex :  6/3 (angka 6 dan 3 adalah sebuah Operand, dan / [bagi] adalah sebuah Operator)
#
# Operator Unary = hanya memiliki satu Operand (positive atau negatif), ex: -10, +20
# Operator Binary = memiliki dua Operand (x,/,+,-), ex = 5+1, 4x4, 10/2
# Operator Ternary = memiliki tiga buah Operand (shorthand untuk percabangan if)
#
# >>Operator Binary :
# Penjumlahan = ' + '
# Pengurangan = ' - '
# Perkalian = ' * '
# Pembagian = ' / '
# Floor Division = ' // '  >> hasil pembagian dimana menghasilkan angka bulat
# Pangkat = ' ** '
#
# >>Operator Perbandingan :
# Sama dengan = ' == '
# Tidak sama dengan = ' != '
# Kurang dari = ' < '
# Lebih dari = ' > '
# Kurang dari sama dengan = ' <= '
# Lebih dari sama dengan = '>= '
#
# >> Operator Logika (Boolean):
# untuk membandingkan sebuah kondisi atau inputan, dengan hasil True / False, umumnya digunakan bersama IF / Loop,
# Operand dari operator logika bertipe integer atau boolean.
#
# and = a and b (True jika kedua data True)
# or = a or b (False jika kedua data False)
# not = (not True menghasilkan False, not False menghasilkan True)
#
# >> Operator Gabungan
# angka += 10 (variabel angka ditambah dengan sepuluh)
# angka -= 10 (variabel angka dikurang dengan sepuluh)
# angka /= 10 (variabel angka dibagi dengan sepuluh)
# angka *= 10 (variabel angka dikali dengan sepuluh)
# angka %= 10 (sisa bagi dari variabel dengan 10 )
# angka **= 10 (variabel angka dipangkatkan dengan sepuluh)
#
# >> Membership
# In = menentukan apakah nilai yang berada di Operand kiri ada di list sebelah kanan, ex : "Halo" in "Halo Dunia"
# not in = menentukan apakah nilai yang berada di Operand kiri tidak ada di list sebelah kanan,
# ex : "Halo" not in "Halo Dunia"
#
# is = menentukan apakah type data benar, ex : type(5) is int = True
# not is = menentukan apakah type data salah, ex : type(5) is not int = False

# >>>>> Fungsi Pada Python
# untuk mengefisiensikan penulisan kode kode dalam pemrograman

# >> Fungsi dengan argumen
# def nama_fungsi(argumen):
#     print("Hallo!")
#     print("Selamat Pagi", argumen)
#     print("Apakah kabarmu hari ini? ")
# nama_fungsi(" Anbiya ")
# nama_fungsi(" Malik ")
# nama_fungsi("Aprian")
# output =
# Hallo!
# Selamat Pagi  Anbiya
# Apakah kabarmu hari ini?
# Hallo!
# Selamat Pagi  Malik
# Apakah kabarmu hari ini?
# Hallo!
# Selamat Pagi Aprian
# Apakah kabarmu hari ini?

# >> Fungsi tanpa argumen
# def nama_fungsi():
#     print("Hallo!")
#     print("Selamat Pagi", )
# nama_fungsi()
# output =
# Hallo!
# Selamat Pagi

# >> Fungsi dengan 2 argumen
# def menghitung_BMI(nama, tinggi, berat):
#     print("Identitas : ", nama, str(tinggi - berat))
# menghitung_BMI("Anbiya", 170, 65)
# menghitung_BMI("Malik", 170, 66)
# menghitung_BMI("Aprian", 170,67)
# output =
# Identitas :  Anbiya 105
# Identitas :  Malik 104
# Identitas :  Aprian 103

# >> jika tidak mengisi value maka bisa di berikan default value
# def selamatPagi(nama = "Sahabatku"):
#     print("Selamat Pagi")
#     print("Hallo ", nama)
#     print("Semoga harimu menyenangkan!")
# selamatPagi("Anbiya")
# selamatPagi()
# output =
# Selamat Pagi
# Hallo  Anbiya
# Semoga harimu menyenangkan!
# Selamat Pagi
# Hallo  Sahabatku
# Semoga harimu menyenangkan!

# def salamPagi(*VarArgs, makan = "kayanya enak makan mie ayam"):
#     print("Hallo!")
#     print("Selamat Pagi, ")
#     for i in VarArgs:
#         print(i,  end = '')
#         print("mau makan apa ? : ", makan)
# salamPagi("Anbiya ", "Malik ", "Aprian")
# output =
# Hallo!
# Selamat Pagi,
# Anbiya mau makan apa ? :  kayanya enak makan mie ayam
# Malik mau makan apa ? :  kayanya enak makan mie ayam
# Aprianmau makan apa ? :  kayanya enak makan mie ayam

# Pengertian Arbitrary Arguments (*args) Python
# Arbitrary arguments adalah istilah untuk menyebut jumlah argumen yang tidak bisa ditentukan atau berubah-ubah.

# >> return (perlu untuk memanggil kembali hasil operand diluar fungsi)

# def hitungBMI(berat, tinggi):
#     return berat / (tinggi * tinggi)
# print("BMI anda adalah : ", hitungBMI(70,1.65))
# outpur = BMI anda adalah :  25.71166207529844

# >> perbandingan pake return dan ngga pake return
# def kuadrat(angka):
#     hasil = angka ** 2
#     return hasil
# print ("Kuadrat dari 5 adalah", kuadrat(5))
# output = Kuadrat dari 5 adalah 25

# def kuadrat(angka):
#     angka ** 2
# print ("Kuadrat dari 5 adalah", kuadrat(5))
# output = Kuadrat dari 5 adalah None

# >>>>> Bekerja dengan variabel dalam fungsi
# Variabel Global = variabel yang bisa di akses di sepanjang kode
# Variabel Local = variabel yang berada didalam fungsi
#  >> ketika variabel local memiliki nama yang sama dengan variabel global, variabel local menutupi variabel global.
# a = 4  # >> variabel global

# def print_func():
#     a = 17 # >> variabel local
#     print("dalam print_func a = ", a)
# print_func()
# print("diluar print_func a =", a)
# output =
# dalam print_func a =  17
# diluar print_func a = 4

# a_var = 10
# b_var = 15
# c_var = 25
#
# def a_func(a_var):
#     print("dalam a_func a_var = ", a_var)
#     b_var =  100 + a_var
#     d_var = 2 * a_var
#     print("dalam a_func b_var = ", b_var)
#     print("dalam a_func d_var = ", d_var)
#     return b_var + 10
# c_var = a_func(b_var)
# print("dalam a_var = ", a_var)
# print("dalam b_var = ", b_var)
# print("dalam c_var = ", c_var)
# print("dalam d_var = ", d_var)  #>>  error karena dalam function tidak ada variabel d_var


# def a_func(a_var):
#     print("dalam a_func a_var =", a_var)
#     b_var = 100 + a_var
#     d_var = 2 * a_var
#     print("dalam a_func b_var =", b_var)
#     print("dalam a_func d_var =", d_var)
#     return b_var + 10
#
# c_var = a_func(5)  # Memanggil fungsi a_func dengan argumen 5 dan menyimpan hasilnya dalam c_var
# print("dalam c_var =", c_var)


# >>>>> User Input
# >> Menggunakan Input (apapun yang di-input user tetap akan bertipe string)
# nama = input("Masukan nama lengkap anda: ")
# print("Nama lengkap anda adalah ", nama, "dengan ", len(nama), "karakter")
# output =
# Masukan nama lengkap anda: Muhammad Anbiya Fatah
# Nama lengkap anda adalah  Muhammad Anbiya Fatah dengan  21 karakter

# >>>>> Perulangan Pada Python
# >> Perulangan While
# a = 0
# while a < 10:
#     a = a + 1
#     print(a)
# output =
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# a = 1
# s = 0
#
# print('Masukan angka untuk ditambahkan.')
# print('Masukan 0 untuk keluar')
#
# while a != 0:
#     print('Jumlah: ', s)
#     a = float(input('Angka ?'))
#     s =  s + a
# print('Jumlah Total = ', s)
# Masukan angka untuk ditambahkan.
# Masukan 0 untuk keluar
# Jumlah:  0
# Angka ?65
# Jumlah:  65.0
# Angka ?78
# Jumlah:  143.0
# Angka ?0
# Jumlah Total =  143.0

# >>>>> Perulangan For
#    1. harus memnuat kondisi jumlah perulangan dan bagian kode yang akan di ulang.
#    2. perulangan akan dilakukan sebanyak angka di dalam range atau list
#    3. baris for wajib diakhiri dengan tanda titik dua
#    4. bagian kode for ditulis dengan lebih menjorok

# satuSampaiSepuluh = range(1, 11)
# for count in satuSampaiSepuluh:
#     print(count)
# output =
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# >> Break
# break adalah kata kunci untuk menghentikan perulangan jika ditemukan kondiri tertentu
# for i in range(1, 21):
#     if i == 10:
#         break
#     print(i)
# output =
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# > Continue
# continue digunakan untuk menjeda perulangan jika kondisi tertentu dicapai.
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)
# output = \
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# >> Perulangan For untuk List
# list adalah variabel yang mengandung banyak nilai

# anggotaKelas = ["anbiya", 23, "Mugis", 23, "Danil", 23]
# for i in anggotaKelas:
#     print("Data nama atau tahun lulus TI23F : ", i)
# output =
# Data nama atau tahun lulus TI23F :  anbiya
# Data nama atau tahun lulus TI23F :  23
# Data nama atau tahun lulus TI23F :  Mugis
# Data nama atau tahun lulus TI23F :  23
# Data nama atau tahun lulus TI23F :  Danil
# Data nama atau tahun lulus TI23F :  23

# BAB 7 : Hal 89.

