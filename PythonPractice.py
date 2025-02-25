import random



####################################################################################################################
####################################################################################################################

# # buat ngitung total honor yang bakal di ambil dari uang transport uang makan uang lembur (dua kondisional)
# # uang lembur di dua jam pertama otu = 100.000/jam , jam berikutnya 150.000/jam
# # dan ada gaji pokok yang bisa di input

# gajiPokok = int(input("Masukan Gaji Pokok Anda : "))
# hariKerja = int(input("Masukan Hari Kerja Anda : "))
# lembur = int(input("Masukan Total Lembur Anda : "))


# totalTransport = 100_000 * hariKerja
# totalMakan = 50_000 * hariKerja


# if lembur <= 2:
#     totalLembur = lembur * 100_000
# else:
#     totalLembur = 200_000 + (lembur - 2) * 150_000
    
# honor = gajiPokok + totalTransport + totalMakan + totalLembur
# print("Jadi Total Honor Anda Adalah %i Rupiah"%honor)


# # kenapa harus pake int input, karena tipe data yang dibutuhkan angka
# # kenapa kali hari kerja, agar membuat dia lebih fleksibel
# # kenapa pake if else, karena ada kondisi kondisi yang harus di perhatikan.

####################################################################################################################
####################################################################################################################

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
# between 1500 and 2700 (both included)

# isNumber = int(input("input the number : "))

# if isNumber >= 1500 and isNumber <= 2700:
#     if isNumber % 7 == 0 and isNumber % 5 == 0:
#         print("number %i can divisible by 7 and multiples of 5"%isNumber)
#     else:
#         print("number %i is not divisible by 7 and multiples of 5"%isNumber)
# else:
#     print("number is not available between 1500 and 2700")    

#####################################################################################################################
#####################################################################################################################

# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
    
    
# isTemperature = input("choose the temperature between celsius and fahrenheit : ")
# isDegrees = int(input("enter the temperature degrees : "))

# if isTemperature == "celsius":
#     isResult = "fahrenheit"
#     convert = (isDegrees *9/5) + 32
# else:
#     isTemperature = "fahrenheit"
#     isResult = "celsius"
#     convert = (isDegrees - 32) * 5/9
    
# print("result of converting the tempreture %s to %s is %i degrees"%(isTemperature, isResult, convert))
    
#####################################################################################################################
#####################################################################################################################


# isAnswer, isGuess = random.randint(0,10), 0

# while isGuess != isAnswer:
#     isGuess = int(input("guess the number between 1-9 : "))

# print("well guess, the secter number is %i"%isAnswer)

#####################################################################################################################
#####################################################################################################################


# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# length = int(input("enter the length of the triagle : "))


# for i in range(1, length + 2):
#     for j in range(0, i):
#         print("* ", end="")
#     print(' ')
# for k in range(length, 0, - 1):
#     for l in range(0, k):
#         print("* ", end="")
#     print(' ')
    
#####################################################################################################################
#####################################################################################################################

#  Write a Python program that accepts a word from the user and reverses it.

# isWord = input("enter the word that you want to reversed : ")
# for char in isWord[::-1]:
#     print(char , end=" ")

# isWord = input("enter the word that you want to reversed : ")

# for i in range(len(isWord)-1, -1, -1):
#     print(isWord[i], end=" ")


#####################################################################################################################
#####################################################################################################################

















