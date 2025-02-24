# Mengatur tinggi belah ketupat
tinggi = 4
x = int(input("masukan nilai x : "))


for i in range(x-3):
    for j in range(x - i - 4):
        print(" ", end=" ")
    for k in range(i * 2 + 1):
        print("*", end=" ")
    print()
    
for i in range(x - 5, -1, -1):
    for j in range(x - i - 4):
        print(" ", end=" ")
    for k in range(i * 2 + 1):
        print("*", end=" ")
    print()
