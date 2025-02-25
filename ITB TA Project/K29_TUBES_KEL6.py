#TUGAS BESAR PENGENALAN KOMPUTASI
#KELOMPOK 6 K29 FTI
#ANGGOTA: 
#1. ADINDA NUR FADILAH 16723360
#2.  FRANCSISCA ARMANDA 16723374
#3. MAZAYA JASMINE SALMARETHA 16723384
#4. SALVAH HARIANTI 16723388
#5. RANY CAROLINA RIEZKY A.E. 16723402
#6. NOVI CRISYANTI 16723432

#TEMA : ATM 

#SIMULASI ATM SEDERHANA 

#data username dan password
import random 
import datetime as dt #impor untuk mendapatkan waktu


tgl = dt.datetime.now() #Untuk menampilan tanggal dan waktu secara otomatis
kode = random.randrange(1,10000000) #kode untuk transaksi
user_id = 0
loop = "n"
users = [
    {
        "id":"1111",
        "no_rekening": "16723360",
        "username" : "ADINDA NUR FADILLAH",
        "pin":"6060",
        "saldo" : 150000
    }, 
    {
        "id":"2222",
        "no_rekening": "16723374",
        "username" : "FRANCSISCA ARMANDA",
        "pin":"7474",
        "saldo" : 150000
    }, 
    {
        "id":"3333",
        "no_rekening": "16723384",
        "username" : "MAZAYA JASMINE S.",
        "pin":"8484",
        "saldo" : 150000
    }, 
    {
        "id":"4444",
        "no_rekening": "16723388",
        "username" : "SALVAH HARIANTI",
        "pin":"8888",
        "saldo" : 150000
    }, 
    {
        "id":"5555",
        "no_rekening": "16723402",
        "username" : "RANY CAROLINA",
        "pin":"1717",
        "saldo" : 100000000
    },
    {
        "id":"6666",
        "no_rekening": "16723432",
        "username" : "NOVI CRISYANTI",
        "pin":"3232",
        "saldo" : 100000000
    }
]
status_login = False
pakai_atm = "y"

def cek_login(p): #Jika pin sesuai dengan yang sudah terdaftar, maka sudah berhasil login
    for user in users:
        if user['pin']==p:
            return user
    return False

def cek_user(id): #Jika nama pengguna sudah sesuai bisa lanjut transaksi
    for i in range(len(users)):
        if users[i]['id']==str(id):
            return int(i)
    return -1

def cek_rekening(no): #Mengidentifikasi agar rekening sudah sesuai
    for i in range(len(users)):
        if str(users[i]['no_rekening'])==str(no):
            return int(i)
    return -1

def transfer_uang(uang, no_rekening): #Fungsi untuk transfer
    indeks1 = cek_user(user_id)
    indeks2 = cek_rekening(no_rekening)
    if indeks1 >= 0:
        if users[indeks1]['saldo'] >= int(uang):
            users[indeks1]['saldo']= users[indeks1]['saldo'] - int(uang)
            users[indeks2]['saldo']= users[indeks2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp. " + str(uang) + " ke Rekening " + no_rekening)
            print("Sisa Saldo Anda adalah Rp. ", users[indeks1]['saldo'])
            print(f'''
                ----------------------------------------
                                                BANK ITB
                           Transaksi Berhasil
                ----------------------------------------
                \tTransfer kepada {no_rek}
                \tSebesar Rp{nominal}
                ----------------------------------------
                Detail Penerima 
                \tNama              : {unama}
                \tMetode Pembayaran : Bank ITB
                \tATM Tujuan        : {atm}

                | ||| || |||| ||| |  || || ||| | | ||| ||
                tanggal     : {tgl}

                Total Pembayaran  : {nominal}
                Kode Transaksi    : {kode}
                ----------------------------------------
                ''')
            print("Sisa saldo Anda adalah Rp.", users[indeks1]['saldo'])
        else:
            print("Saldo Anda tidak cukup.")



def ambil_uang(uang): #Fungsi untuk tarik tunai
    indeks1 = cek_user(user_id)
    if indeks1 >= 0:
        if users[indeks1]['saldo']>= int(uang):
            print("Silahkan pilih pecahan uang yang Anda inginkan:")
            print("a. Rp 20.000")
            print("b. Rp 50.000")
            print("c. Rp 100.000")
            pecahan = int(input("Pecahan uang yang diinginkan (tulis nominal saja): "))
            
            if  int(uang)%pecahan == 0:
                masuk = int(uang)//pecahan

                print(f'Jumlah uang Rp{pecahan}: {masuk} lembar.')
                users[indeks1]['saldo' ]= users[indeks1]['saldo'] - int(uang)
                print(f'''
                    ----------------------------------------
                                                     BANK ITB
                             Transaksi Berhasil
                    ----------------------------------------
                    \tTANGGAL    WAKTU  
                    \t{tgl}
                    ----------------------------------------
                    PENARIKAN RP. {int(uang)}
                    
                    SALDO REK. RP. {users[indeks1]['saldo']}

                    | ||| || |||| ||| |  || || ||| | | ||| ||

                    Kode Transaksi    : {kode}
                    ----------------------------------------
                    ''')
                print("----- PENARIKAN BERHASIL -----")
                print("Sisa saldo Anda adalah Rp. ", users[indeks1]['saldo'])
            else: 
                print("Nominal pecahan tidak sesuai. Silakan pilih nominal lain.")
            
        else:
            print("Saldo Anda tidak cukup.")

def setor_uang(uang): #Fungsi untuk penyetoran tunai
    indeks1 = cek_user(user_id)
    if indeks1 >= 0:
        print("-"*40)
        print("Silahkan masukkan uang yang akan disetor: ")
        print("Nominal yang diterima")
        print("a. Rp 20.000")
        print("b. Rp 50.000")
        print("c. Rp 100.000")
        setoran = int(input("Nominal yang akan disetor: "))
        print("-"*40)
        if setoran <=19999:
            print("Nominal terlalu kecil.")
        elif (setoran%20000) == 0 or (setoran%50000)==0 or setoran%100000 == 0:
            duapuluh = int(input("Lembar uang kertas Rp 20.000 :"))
            limapuluh = int(input("Lembar uang kertas pecahan Rp 50.000 : "))
            seratus = int(input("Lembar uang kertas pecahan Rp 100.000 : "))

            totaluang = ((duapuluh)*20000) + ((limapuluh)*50000) + ((seratus)*100000)
            if totaluang != int(uang):
                print("Terjadi kesalahan.")
            else:
                users[indeks1]['saldo']= users[indeks1]['saldo'] + totaluang
                print("\n")
                print(f'''
                    ----------------------------------------
                                                     BANK ITB
                                Transaksi Berhasil
                    ----------------------------------------
                    TANGGAL    WAKTU  
                    {tgl}
                    ----------------------------------------
                    PENYETORAN RP. {int(uang)}
                    
                    SALDO REK. RP. {users[indeks1]['saldo']}

                    | ||| || |||| ||| |  || || ||| | | ||| ||

                    Kode Transaksi    : {kode}
                    ----------------------------------------
                    ''')
                print("---Setor Tunai Berhasil!---")
                print("Saldo Anda saat ini: ", users[indeks1]['saldo'] , end=" ")
                print("-/Rupiah\n\n")
        
        else: 
            print("Tidak dapat menerima uang.")

while pakai_atm == "y":
    while not status_login:
        print("---- SELAMAT DATANG DI ATM ITB -----")
        print("\n")
        print("SILAKAN MASUKKAN PIN ANDA")
        pin = input("MASUKKAN PIN : ")
        print("\n")
        print("-"*40)
 
        cl = cek_login(pin)
        if cl:
            print("Login berhasil.")
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops PIN anda salah")
            print("")
            print("")
 
    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("----- SELAMAT DATANG DI ATM ITB -----")
        print("=<<    1. CEK SALDO    >>=")
        print("=<<    2.TRANSFER       >>=")
        print("=<<    3. TARIK TUNAI   >>=")
        print("=<<    4. SETOR TUNAI   >>=")
        print("=<<    5. KELUAR        >>=")
        a = int(input("Silahkan pilih menu : "))
        print("-"*40)
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)
            unama = input("Nama Singkat: ")
            atm = input("ATM Tujuan: ")
            

 
            if cnk >= 0:
                print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                nominal = input("Nominal Yang Akan Di Transfer : ")
                transfer_uang(nominal, no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
 
        elif a == 3:
            nominal = input("Nominal Yang Akan Ditarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            nominal = input("Nominal Yang Akan Disetor: ")
            setor_uang(nominal)
 
        elif a == 5:
            print("Terima kasih sudah menggunakan ATM ITB!")
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("Pilihan tidak tersedia")
        if status_login == True:
            input("Kembali Ke menu (Enter) ")
            print("")
            loop = "y"
