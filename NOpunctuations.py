#buatlah program untuk memisahkan integer dan string dari sebuah inputan.

# angka = "1234567890"
# Integer = ""
# String = ""
# text = input("masukan inputan : ")

# for char in text:
#     if char not in angka:
#         String = String + char
#     else:
#         Integer = Integer + char
        
# print(Integer)
# print(String)


Integer = ""
String = ""
text = input("masukan inputan : ")

for char in text:
    if char.isdigit():  #untuk ngecek apakah character angka
        Integer += char
    elif char.isalpha(): #untuk ngecek apakah character huruf
        String += char

print(Integer,"\n",String)