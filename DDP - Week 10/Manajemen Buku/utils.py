from models import dataBuku

listMahasiswa = []
listPeminjaman = []

def tambah_mahasiswa(nama, nim, nomerhp, alamat):
    mahasiswa = {
        'nama': nama,
        'nim': nim,
        'nomerhp': nomerhp,
        'alamat': alamat
    }
    listMahasiswa.append(mahasiswa)
    print()
    print("Mahasiswa ditambahkan")

def tambah_peminjaman(nim, no_isbn, tanggalpinjam, tanggal_kembali, status):
    peminjaman = {
                    'nim': nim,
                    'no_isbn': no_isbn,
                    'tanggalpinjam': tanggalpinjam,
                    'tanggal_kembali': tanggal_kembali,
                    'status': status
                }
    listPeminjaman.append(peminjaman)
    
    cekNim = any(mhs['nim'] == nim for mhs in listMahasiswa)
    if not cekNim:
        print()
        print("NIM yang dimasukkan tidak ditemukan")
        return
            
    for buku in dataBuku:
        if buku['no_isbn'] == no_isbn:
            if buku['stok'] > 0:
                buku['stok'] -= 1
                buku['booked'] += 1
                print()
                print("Peminjaman berhasil ditambahkan")
                break
            else:
                print()
                print("Stok buku habis, silakan pilih buku lain")
                break
        else:
            print()
            print("Buku dengan ISBN tersebut tidak ditemukan!")
            break

                    
        
def tampilkan_peminjaman():
    if not listPeminjaman:
        print("Tidak ada peminjaman yang terdaftar.")
        return
    
    for peminjaman in listPeminjaman:
        for mahasiswa in listMahasiswa:
            if peminjaman['nim'] == mahasiswa['nim']:
                print()
                print(f"Mahasiswa: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Nomor HP: {mahasiswa['nomerhp']}, Alamat: {mahasiswa['alamat']}")
                for buku in dataBuku:
                    if buku['no_isbn'] == peminjaman['no_isbn']:
                        print(f"Peminjaman: {buku['judul']}, Tanggal Pinjam: {peminjaman['tanggalpinjam']}, Tanggal Kembali: {peminjaman['tanggal_kembali']}, Status: {peminjaman['status']}")

def tampilkan_data():
    for buku in dataBuku:
        print(f"ISBN: {buku['no_isbn']}, Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Halaman: {buku['isihalaman']}, Deskripsi: {buku['deskripsi']}, Stok: {buku['stok']}, Booked: {buku['booked']}")



