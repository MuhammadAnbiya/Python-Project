from tkinter import *
import time
from tkinter import messagebox
import random
import datetime as dt
kode = random.randrange(100,10000)

root = Tk()
root.geometry("900x850")
root.title("MESIN ATM")
root.configure(bg="blue")

Tops = Frame(root, bg="blue", width=800, height=50, relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root, bg="blue", width=300, height=700, relief=SUNKEN)
f1.pack(side=LEFT)
f2 = Frame(root, bg="blue", width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="ATM ITB", fg="black", bg="blue", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20), text=localtime, fg="black", bg="blue", anchor=W)
lblinfo.grid(row=1, column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
form = False
acca = 0
amo = 0
wd = 0
result = 0
dep = 0

def bank():
    global acca, form, number_input, bank_info
    accno = ["16723360","16723374","16723384","16723388", "16723402",  "16723432"]
    account = number.get()
    number_input = number.get()
    if number_input:
        if account in accno:
            form = True
            label.config(text="PIN Benar")
            bank_info = {"16723360":100000,"16723374": 200000,"16723384":300000,"16723388":400000, "16723402":500000,  "16723432":600000}
            balance = bank_info[account]
            acca = balance
        else:
            label.config(text="PIN anda salah")
    else:
        label.config(text="Masukkan PIN")


def deposit():
    global amount_input,amo, dep
    amount_input = amount.get()
    if form == True:
        if amount_input:
            amo = float(amount_input)
            dep = acca + amo
            label3.config(text=("Saldo anda:", str(dep)))
            messagebox.showinfo("Info", f'''
                    ----------------------------------------
                                                     BANK ITB
                             Transaksi Berhasil
                    ----------------------------------------
                    TANGGAL    WAKTU  
                    {localtime}
                    ----------------------------------------
                    PENYETORAN RP. {amo}
                    
                    SALDO REK. RP. {dep}

                    | ||| || |||| ||| |  || || ||| | | ||| ||

                    Kode Transaksi    : {kode}
                    ----------------------------------------
                    ''')
        else:
            label3.config(text=("Silakan masukkan nominal"))
    else:
        label3.config(text=("Silakan masukkan PIN terlebih dahulu"))


def withdrawn():
    global wd_input,wd, acca
    wd_input = withd.get()
    if form == True:
        if wd_input:
            wd = float(wd_input)
            if dep >= wd:
                ace = dep - wd
                label4.config(text=("Saldo anda:", str(ace)))
                messagebox.showinfo("Info", f'''
                    ----------------------------------------
                                                     BANK ITB
                             Transaksi Berhasil
                    ----------------------------------------
                    TANGGAL    WAKTU  
                    {localtime}
                    ----------------------------------------
                    PENARIKAN RP. {wd}
                    
                    SALDO REK. RP. {ace}

                    | ||| || |||| ||| |  || || ||| | | ||| ||

                    Kode Transaksi    : {kode}
                    ----------------------------------------
                    ''')
            else:
                label4.config(text=("Mohon maaf saldo anda tidak cukup:", str(dep)))
        else:
            label4.config(text=("Silahkan masukkan nominal"))
    else:
        label4.config(text=("Silakan masukkan PIN terlebih dahulu"))


def bal():
    global result
    if form == True:
        if dep >= wd:
            result = acca + amo - wd
            label5.config(text=("Saldo anda:", str(result)))
        else:      
            label5.config(text=("Saldo anda:", str(dep)))

    else:
        label5.config(text=("Saldo anda:", str(acca)))
        

def reset():
    global form, acca, amo, wd
    form = False
    acca = 0
    amo = 0
    wd = 0
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")



lbl = Label(f1, font=('aria', 16, 'bold'), text="Masukkan PIN:        ", bg="blue", fg="black",
            bd=10, anchor='w')
lbl.grid(row=0, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=number, bd=6, insertwidth=4, fg="black", justify='right')
txt.grid(row=0, column=4)
label = Label(f1, fg="black", bg="blue", font=('aria', 16, 'bold'))
label.grid(row=1, column=4)
btnsubmit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="SUBMIT",
                   bg="Powder Blue", command=bank)
btnsubmit.grid(row=0, column=4)

lblTotal = Label(f1, text="                     ", fg="black", bg="blue")
lblTotal.grid(row=3, columnspan=10)

lbl = Label(f1, font=('aria', 16, 'bold'), text="Masukkan nominal setoran:          ", bg="blue", fg="black",
            bd=10, anchor='w')
lbl.grid(row=4, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=amount, bd=6, insertwidth=4, bg="white", justify='right')
txt.grid(row=4, column=4)
label3 = Label(f1, fg="black", bg="blue", font=('aria', 16, 'bold'))
label3.grid(row=5, column=4)
btndeposit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="SETOR",
                    bg="Powder Blue", command=deposit)
btndeposit.grid(row=4, column=4)

lblTotal = Label(f1, text="                             ", fg="black", bg="blue")
lblTotal.grid(row=7, columnspan=10)

lbl = Label(f1, font=('aria', 16, 'bold'), text="Masukkan nominal penarikan:        ", bg="blue",
            fg="black", bd=10, anchor='w')
lbl.grid(row=8, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=withd, bd=6, insertwidth=4, bg="white", justify='right')
txt.grid(row=8, column=4)
label4 = Label(f1, fg="black", bg="blue", font=('aria', 16, 'bold'))
label4.grid(row=9, column=4)
label5 = Label(f1, fg="black", bg="blue", font=('aria', 16, 'bold'))
label5.grid(row=10, column=4)

btnwithdraw = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="TARIK",
                     bg="Powder Blue", command=withdrawn)
btnwithdraw.grid(row=8, column=4)
btnbal = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="SALDO",
                bg="Powder Blue", command=bal)
btnbal.grid(row=10, column=4)
btnreset = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="RESET",
                  bg="Powder Blue", command=reset)
btnreset.grid(row=11, column=4)
btnexit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="KELUAR",
                 bg="Powder Blue", command=root.destroy)
btnexit.grid(row=12, column=4)

root.mainloop()
