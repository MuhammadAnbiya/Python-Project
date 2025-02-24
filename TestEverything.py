# # tempat nyoba code berhasil atau ngga dan nemu syntax baru

## >>>>> (list, tuple, set, dict)
# >> list --> diapit dengan kurung siku "[]"  dan dipisahkan dengan tanda koma ","
# list = ["anbiya" , 22, "september"]
# print(list[1])
# # output = 22

# >> tuple --> diapit dengan kurung biasa "()"  dan dipisahkan dengan tanda koma ","
#      >> data dari tuple tidak dapat di ubag (immutable )    
# himpunan = (453, "adalah orang " , "aqua", 7676)
# print(himpunan[1:3])   >>> data di ambil dari urut 1 dan sebelum 3
# output = ('adalah orang ', 'aqua')

# >> set --> diapit dengan kurung kurawal "{}"  dan dipisahkan dengan tanda koma ","
#      >> tipe data objek tidak mengizinkan adanya elemen dengan nilai yang sama dan 
#         tidak memperdulikan urutan dari elemen.
# variabel = "JAKARTA"
# print(set(variabel))
# output = {'R', 'J', 'A', 'K', 'T'}

# >> dict --> diapit dengan kurung kurawal "{}"  dan dipisahkan dengan tanda koma ","
#      >> Setiap elemen pada tipe data dictionary dideklarasikan dengan format:
#         ("kunci" : "nilai")
#          Hal inilah yang membedakan tipe dta dictionary dengan tipe data set. 
#          Kunci ini dapat dijadikan sebagai indeks, sehingga nilainya harus unique.
# data = { "nama:" : "anbiya" , "pekerjaan" : "mahasiswa" , "umur" : "19 tahun" }
# print(data["nama:"])
# print(data["pekerjaan"])
# outpuy = anbiya
#          mahasiswa



# >>>>> sorted & sort (mengurutkan abjad dari a-z dan dari z-a)
# >> mengurutkan dari a-z pake sorted
# abjad = ['d','A','e', 'b','E','c']
# abjad_urut = sorted(abjad)
# print(abjad_urut)
# output = ['A', 'E', 'c', 'd', 'eb'] >>> hruuf besar diurutkan lebih dahulu
# >> mengurutkan dari a-z pake sort
# abjad = ['d','A','e', 'b','E','c']
# abjad.sort()
# print(abjad)
# output = ['A', 'E', 'b', 'c', 'd', 'e']

# >> mengurutkan dari z-a pake sort
# abjad = ['d','A','e', 'b','E','c']
# abjad.sort(reverse=True)
# print(abjad)
# output = ['e', 'd', 'c', 'b', 'E', 'A']  >>> diurutkan terbalik 


## >>>>> perulangan 2x
# r = dict()
# for i in range(3):
#     r[i] = int(input("Enter any value="))

# for i in range(3):
#     print(f"Your {i} value = {r[i]}")
# output = 
# Enter any value=3
# Enter any value=4
# Enter any value=6
# Your 0 value = 3
# Your 1 value = 4
# Your 2 value = 6


## >>>>> Len

# tiF = ("anbiya" , "mughis" , "rizal")
# print(len(tiF))
# output = (3)
# nilai_kalkulus = (90, 99, 89, 87, 97)
# banyak_nilai = len(nilai_kalkulus)
# print(banyak_nilai)
# output = (5)


## >>>>> perulangan (for dan while)

# ulang = 3

# for i in range(ulang):
#     print(f"Perulangan ke-{i}")
# output = ( Perulangan ke- 0
#            Perulangan ke- 1
#            Perulangan ke- 2 )

# item = ['kopi','nasi','teh','jeruk']

# for isi in item:
#     print(isi)
# output = nasi
#          teh
#          jeruk


## >>>>> (sort dan reverse) untuk mengurutkan angka dari besar ke kecil dan kecil ke besar.
# >> sorted
# a1 = 3
# a2 = 4
# a3 = 5
# x = [a1, a2, a3]
# y = sorted(x)
# print(y)
# output [3, 4, 5]
        
# >> reverse        
# luas = [2, 4, 10, 3, 45, 22, 100]
# luas.reverse()
# print(luas)
# output = [100, 22, 45, 3, 10, 4, 2]


## >>>>> ctrl + shift + L 
# untuk mengubah variabel secara bersamaan


## >>>>> fungsi dari 'f' pada (f"Masukan angka ke-{i} :")

# for i in range(1, 4):
#     user_input = input(f"Masukan angka ke-{i} :")
#     r.append(float(user_input))  # Convert user input to float for numerical operations

# kenapa pada user input menggunakan f sebelum string Masukan angka ke-{i}

# Pada contoh kode yang Anda berikan, f-string digunakan untuk memasukkan nilai dari 
# variabel i ke dalam string f"Masukan angka ke-{i} :". Ini adalah fitur yang diperkenalkan 
# dalam Python 3.6 dan memungkinkan Anda menyisipkan nilai variabel ke dalam string dengan mudah.

# Misalnya, ketika i bernilai 1, f-string tersebut akan diinterpretasikan sebagai "Masukan angka ke-1 :", 
# dan ketika i bernilai 2, maka f-string akan menjadi "Masukan angka ke-2 :", dan seterusnya. Ini membuat 
# pesan input menjadi lebih dinamis tanpa perlu melakukan konkatenasi string manual.

# F-string sangat berguna dalam situasi di mana Anda perlu menggabungkan nilai variabel ke dalam string 
# tanpa banyak penulisan kode untuk menggabungkan string dan variabel secara terpisah. Ini membuat kode 
# lebih mudah dibaca dan lebih efisien.

