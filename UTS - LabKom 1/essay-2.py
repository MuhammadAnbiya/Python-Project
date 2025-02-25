
# N * * * * * *
# N U * * * * *
# N U G * * * *
# N U G R * * *
# N U G R A * *
# N U G R A H *
# N U G R A H A

nama = input("Masukan nama anda yang ingin dicek : ") 
for i in range(0,len(nama)):
    for j in range(0,len(nama)):
        if j < i+1: 
            print(nama[j], end=" ")
        else:
            print("*", end=" ")
    print()


