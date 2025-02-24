# Buatlah aplikasi manajemen buku dengan menggunakan list dan dictionary, setiap buku terdiri dari (no_isbn, judul, pengarang, isihalaman, deskripsi, stok, booked).
# Lalu ada list mahasiswa (nama, nim, nomerhp, alamat)
# Lalu ada list peminjam (nim, no_isbn, tanggalpinjam, tanggal_kembali, status)

from utils import *

while True:
    print()
    print("Selamat datang pada aplikasi Manajemen Buku Genusian!" + "\n" 
      + "Silahkan pilih nomor untuk memulai : " + "\n"
      + "1. Tampilkan data buku" + "\n"
      + "2. Tambah mahasiswa" + "\n"
      + "3. Tambah peminjaman" + "\n"
      + "4. Tampilkan peminjaman" + "\n"
      + "5. Exit")
    choice = input("Masukkan pilihan: ")

    if choice == '1':
        print()
        print("Berikut adalah data buku yang tersedia:")
        tampilkan_data()

    elif choice == '2':
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        nomerhp = input("Masukkan nomor HP: ")
        alamat = input("Masukkan alamat: ")
        tambah_mahasiswa(nama, nim, nomerhp, alamat)

    elif choice == '3':
        nim = input("Masukkan NIM: ")
        no_isbn = input("Masukkan ISBN: ")
        tanggalpinjam = input("Masukkan tanggal pinjam: ")
        tanggal_kembali = input("Masukkan tanggal kembali: ")
        status = input("Masukkan status: ")
        tambah_peminjaman(nim, no_isbn, tanggalpinjam, tanggal_kembali, status)
        
    elif choice == '4':
        print()
        print("Berikut adalah data peminjaman terbaru:")
        tampilkan_peminjaman()

    elif choice == '5':
        break