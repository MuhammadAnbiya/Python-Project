from tkinter import *
import tkinter.font as font  # imports font module and being imported as font. It helps to define a specific font style
import random

win = Tk()  # creates the window
win.title('ATM')
win.geometry('600x600')  # sets the dimension of the window

tim40 = font.Font(family='Times', size=40, weight='bold', slant='italic',
                  underline=1)  # Font is an instance which contains parameter as
# family(the font style), size, weight(bold,normal)
# slant(italic,roman(non-italic)), underline(1-yes,0-no),
# overstrike(1-yes,0-no) and many more
cour20 = font.Font(family='Courier', size=20, weight='bold')
cour15 = font.Font(family='Courier', size=15, weight='bold')

glob_count = 0

# FUNGSI FUNGSI YANG DIBUTUHKAN
users = {
        "id": 1234,
        "no_rekening": 1234567890,
        "nama_singkat": "Eryn",
        "pin": 4321,
        "saldo": 45550
    }


def set_user_data(nama, pin, saldo):
    users['nama_singkat'] = nama
    users['pin'] = pin
    users['saldo'] = saldo


def option_func():
    win.withdraw()  # check enter_pin() function for the functionality of .withdraw()
    option_func.option_win = Toplevel(win)
    option_func.option_win.geometry('600x600')
    # option_win.grab_set()                       ## check enter_pin() function for the functionality of .grab_set()

    text_title = Label(option_func.option_win, text='\nATM', font=tim40)
    text_title.pack()

    rf = Frame(option_func.option_win)  # right frame
    rf.pack(side=RIGHT)

    lf = Frame(option_func.option_win)  # left frame
    lf.pack(side=LEFT)

    center = Frame(option_func.option_win)
    center.pack(side=LEFT)

    cek_saldo_btn = Button(rf, text='   CEK SALDO   ', font=cour15, command=(ceksaldo))
    cek_saldo_btn.pack(padx=40, pady=10)

    transfer_btn = Button(rf, text='   TRANSFER   ', font=cour15, command=())
    transfer_btn.pack(padx=40, pady=10)

    tarik_tunai_btn = Button(lf, text='  TARIK TUNAI  ', font=cour15, command=(penarikan))
    tarik_tunai_btn.pack(padx=40, pady=11)

    setor_tunai_btn = Button(lf, text='   SETOR TUNAI   ', font=cour15, command=())
    setor_tunai_btn.pack(padx=40, pady=11)

    exit_btn = Button(rf, text='   KELUAR   ', font=cour15,
                      command=lambda: [option_func.option_win.destroy(), win.deiconify()])
    exit_btn.pack(padx=40, pady=10, side=BOTTOM)  # check enter_pin() function for the functionality of .deiconify()


def penarikan():
    option_func.option_win.withdraw()
    penarikan.penarikan_win = Toplevel(win)
    penarikan.penarikan_win.geometry('600x600')

    enter_lbl = Label(penarikan.penarikan_win, text='\nMASUKKAN JUMLAH PENARIKAN TUNAI\nYANG ANDA INGINKAN\n',
                      font=cour20, fg='red')
    enter_lbl.pack()
    money_entry = Entry(penarikan.penarikan_win, font=cour15, justify='center')
    money_entry.pack()

    bf = Frame(penarikan.penarikan_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(penarikan.penarikan_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(penarikan.penarikan_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(penarikan.penarikan_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(penarikan.penarikan_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(penarikan.penarikan_win)
    bf1.pack(side=BOTTOM)

    b1 = Button(bf1, text='1', font=cour15, command=lambda: money_entry.insert('end', '1'))
    b1.pack(side=LEFT, pady=10)

    b2 = Button(bf1, text='2', font=cour15, command=lambda: money_entry.insert('end', '2'))
    b2.pack(side=LEFT, padx=10)

    b3 = Button(bf1, text='3', font=cour15, command=lambda: money_entry.insert('end', '3'))
    b3.pack(side=LEFT)

    b4 = Button(bf2, text='4', font=cour15, command=lambda: money_entry.insert('end', '4'))
    b4.pack(side=LEFT)

    b5 = Button(bf2, text='5', font=cour15, command=lambda: money_entry.insert('end', '5'))
    b5.pack(side=LEFT, padx=10)

    b6 = Button(bf2, text='6', font=cour15, command=lambda: money_entry.insert('end', '6'))
    b6.pack(side=LEFT)

    b7 = Button(bf3, text='7', font=cour15, command=lambda: money_entry.insert('end', '7'))
    b7.pack(side=LEFT, pady=10)

    b8 = Button(bf3, text='8', font=cour15, command=lambda: money_entry.insert('end', '8'))
    b8.pack(side=LEFT, padx=10)

    b9 = Button(bf3, text='9', font=cour15, command=lambda: money_entry.insert('end', '9'))
    b9.pack(side=LEFT)

    btn = Button(bf4, text=' ', font=cour15)
    btn.pack(side=LEFT)

    b0 = Button(bf4, text='0', font=cour15, command=lambda: money_entry.insert('end', '0'))
    b0.pack(side=LEFT, padx=10)

    btn_ = Button(bf4, text=' ', font=cour15)
    btn_.pack(side=LEFT)

    enter_btn = Button(bf, text='ENTER', font=cour15, fg='green', command=question_func)
    enter_btn.pack(side=LEFT, pady=10)

    clear_btn = Button(bf, text='CLEAR', font=cour15, fg='orange', command=lambda: money_entry.delete(1))
    clear_btn.pack(side=LEFT, padx=10)

    exit_button = Button(bf, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=LEFT, pady=10)


def question_func():
    global glob_count
    glob_count += 1

    penarikan.penarikan_win.withdraw()
    question_func.question_win = Toplevel(win)
    question_func.question_win.geometry('600x600')

    bf = Frame(question_func.question_win)
    bf.pack(side=BOTTOM)

    msg_box = Message(question_func.question_win, text='\nTransaksi Sukses. \n Cetak struk transaksi?', font=cour20, )
    msg_box.pack()

    yes_btn = Button(bf, text='YES', font=cour15, fg='green', command=())
    yes_btn.pack(side=LEFT, pady=10)

    no_btn = Button(bf, text=' NO ', font=cour15, fg='red', command=(display_func))
    no_btn.pack(pady=10, padx=10)


def display_func():
    question_func.question_win.withdraw()
    display_win = Toplevel(win)
    display_win.geometry('600x600')
    message = Message(display_win, text='\n\nTransaksi berhasil. \nTerima kasih sudah menggunakan Bank', font=cour20, )
    message.pack()
    text = Label(display_win, text='ATM', font=tim40)
    text.pack()

    exit_button = Button(display_win, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


def ceksaldo():
    global glob_count

    if glob_count == 1:
        question_func.question_win.withdraw()

    option_func.option_win.withdraw()
    balance_win = Toplevel(win)
    balance_win.geometry('460x390')
    # balance_win.grab_set()
    balance = random.randrange(100, 10000)
    message = Message(balance_win, text='\nSaldo Anda saat ini: ' + str(balance) + '\nKembali ke halaman awal?',
                      font=cour20)
    message.pack()

    exit_button = Button(balance_win, text='EXIT', font=cour15, fg='red', command=option_func)
    exit_button.pack(side=BOTTOM, pady=10)


"==============MENU UTAMA========"

"===============HALAMAN UTAMA=========================================="
intro = Label(win, text='\n ---- Selamat Datang di ATM BANK ----', font=cour20, fg='green')
intro.pack()
option_label = Label(win, text=" \nMASUKKAN PIN ATM ANDA", font=cour15, )
option_label.pack()

enter_lbl = Label(win, text='\nDEMI KEAMANAN DAN KENYAMANAN\nSILAKAN GANTI PIN ANDA\nSECARA BERKALA', font=cour20,
                  fg='red')
enter_lbl.pack()
money_entry = Entry(win, font=cour15, show="*", justify='center')
money_entry.pack()
"=================NUMBER PAD==========================================="
bf = Frame(win)
bf.pack(side=BOTTOM)

bf4 = Frame(win)
bf4.pack(side=BOTTOM)

bf3 = Frame(win)
bf3.pack(side=BOTTOM)

bf3 = Frame(win)
bf3.pack(side=BOTTOM)

bf2 = Frame(win)
bf2.pack(side=BOTTOM)

bf1 = Frame(win)
bf1.pack(side=BOTTOM)

b1 = Button(bf1, text='1', font=cour15, command=lambda: money_entry.insert('end', '1'))
b1.pack(side=LEFT, pady=10)

b2 = Button(bf1, text='2', font=cour15, command=lambda: money_entry.insert('end', '2'))
b2.pack(side=LEFT, padx=10)

b3 = Button(bf1, text='3', font=cour15, command=lambda: money_entry.insert('end', '3'))
b3.pack(side=LEFT)

b4 = Button(bf2, text='4', font=cour15, command=lambda: money_entry.insert('end', '4'))
b4.pack(side=LEFT)

b5 = Button(bf2, text='5', font=cour15, command=lambda: money_entry.insert('end', '5'))
b5.pack(side=LEFT, padx=10)

b6 = Button(bf2, text='6', font=cour15, command=lambda: money_entry.insert('end', '6'))
b6.pack(side=LEFT)

b7 = Button(bf3, text='7', font=cour15, command=lambda: money_entry.insert('end', '7'))
b7.pack(side=LEFT, pady=10)

b8 = Button(bf3, text='8', font=cour15, command=lambda: money_entry.insert('end', '8'))
b8.pack(side=LEFT, padx=10)

b9 = Button(bf3, text='9', font=cour15, command=lambda: money_entry.insert('end', '9'))
b9.pack(side=LEFT)

btn = Button(bf4, text=' ', font=cour15)
btn.pack(side=LEFT)

b0 = Button(bf4, text='0', font=cour15, command=lambda: money_entry.insert('end', '0'))
b0.pack(side=LEFT, padx=10)

btn_ = Button(bf4, text=' ', font=cour15)
btn_.pack(side=LEFT)

enter_btn = Button(bf, text='ENTER', font=cour15, fg='green', command=option_func)
enter_btn.pack(side=LEFT, pady=10)

clear_btn = Button(bf, text='CLEAR', font=cour15, fg='orange', command=lambda: money_entry.delete(1))
clear_btn.pack(side=LEFT, padx=10)

exit_button = Button(bf, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
exit_button.pack(side=LEFT, pady=10)

win.mainloop()