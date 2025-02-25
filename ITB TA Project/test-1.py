from tkinter import *
import time

root = Tk()
root.geometry("900x850")
root.title("MESIN ATM")
root.configure(bg="black")

Tops = Frame(root, bg="white", width=800, height=50, relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root, bg="black", width=300, height=700, relief=SUNKEN)
f1.pack(side=LEFT)
f2 = Frame(root, bg="black", width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="MESIN ATM", fg="Powder Blue", bg="black", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20), text=localtime, fg="Powder Blue", bg="black", anchor=W)
lblinfo.grid(row=1, column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
form = False
acca = 0
amo = 0
wd = 0
result = 0

def bank():
    global acca, form, number_input, bank_info
    accno = ["16723388", "16723402", "16723384", "16723380"]
    account = number.get()
    number_input = number.get()
    if number_input:
        if account in accno:
            form = True
            label.config(text="Registered member")
            bank_info = {"16723388": 100000, "16723402": 200000, "16723384": 300000, "16723380": 400000}
            balance = bank_info[account]
            acca = balance
        else:
            label.config(text="Non-Registered member")
    else:
        label.config(text="please fill in the blank")


def deposit():
    global amount_input,amo, dep
    amount_input = amount.get()
    if form == True:
        if amount_input:
            amo = float(amount_input)
            dep = acca + amo
            label3.config(text=("Net Balance:", str(dep)))
        else:
            label3.config(text=("please fill in the blank"))
    else:
        label3.config(text=("please input your acc"))


def withdrawn():
    global wd_input,wd
    wd_input = withd.get()
    if form == True:
        if wd_input:
            wd = float(wd_input)
            if dep >= wd:
                ace = acca + amo - wd
                label4.config(text=("Net Balance:", str(ace)))
            else:
                label4.config(text=("Insufficient balance:", str(acca)))
        else:
            label4.config(text=("please fill in the blank"))
    else:
        label4.config(text=("please input your acc"))


def bal():
    global result
    if acca >= wd:
        result = acca + amo - wd
        label5.config(text=("Net Balance:", str(result)))
    else:
        label5.config(text=("Net Balance:", str(acca + amo)))



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



lbl = Label(f1, font=('aria', 16, 'bold'), text="Enter the account number:        ", bg="black", fg="powder Blue",
            bd=10, anchor='w')
lbl.grid(row=0, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=number, bd=6, insertwidth=4, fg="Powder Blue", justify='right')
txt.grid(row=0, column=4)
label = Label(f1, fg="white", bg="black", font=('aria', 16, 'bold'))
label.grid(row=1, column=4)
btnsubmit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="SUBMIT",
                   bg="Powder Blue", command=bank)
btnsubmit.grid(row=0, column=4)

lblTotal = Label(f1, text="                     ", fg="white", bg="black")
lblTotal.grid(row=3, columnspan=10)

lbl = Label(f1, font=('aria', 16, 'bold'), text="Enter the amount to be deposited:", bg="black", fg="powder Blue",
            bd=10, anchor='w')
lbl.grid(row=4, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=amount, bd=6, insertwidth=4, bg="Powder Blue", justify='right')
txt.grid(row=4, column=4)
label3 = Label(f1, fg="white", bg="black", font=('aria', 16, 'bold'))
label3.grid(row=5, column=4)
btndeposit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="DEPOSIT",
                    bg="Powder Blue", command=deposit)
btndeposit.grid(row=4, column=4)

lblTotal = Label(f1, text="                             ", fg="white", bg="black")
lblTotal.grid(row=7, columnspan=10)

lbl = Label(f1, font=('aria', 16, 'bold'), text="Enter the amount to be withdrawn:        ", bg="black",
            fg="powder Blue", bd=10, anchor='w')
lbl.grid(row=8, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=withd, bd=6, insertwidth=4, bg="Powder Blue", justify='right')
txt.grid(row=8, column=4)
label4 = Label(f1, fg="white", bg="black", font=('aria', 16, 'bold'))
label4.grid(row=9, column=4)
label5 = Label(f1, fg="white", bg="black", font=('aria', 16, 'bold'))
label5.grid(row=10, column=4)

btnwithdraw = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="WITHDRAW",
                     bg="Powder Blue", command=withdrawn)
btnwithdraw.grid(row=8, column=4)
btnbal = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="Balance",
                bg="Powder Blue", command=bal)
btnbal.grid(row=10, column=4)
btnreset = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="Reset",
                  bg="Powder Blue", command=reset)
btnreset.grid(row=11, column=4)
btnexit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="Exit",
                 bg="Powder Blue", command=root.destroy)
btnexit.grid(row=12, column=4)

root.mainloop()
