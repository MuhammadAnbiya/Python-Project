# LATIHAN SOAL 

print("No. 1")
    # 1. Aku cinta Indonesia
    # 3. Aku cinta Indonesia
    # 5. Aku cinta Indonesia
    
a = 1
for i in range(3):
    print(f"{a}.", "Aku cinta indonesia")
    a += 2


print(" ")
print("No. 2")
    # (2 4 7 11 16 22)
    
a = 2
b = 1
for i in range(6):
    print(a, end= " ")
    b += 1
    a += b


print(" ")
print(" ")
print("No. 3")
    # 1 x 1 = 1
    # 1 x 2 = 2
    # 1 x 3 = 3

a = 1
for i in range(3):
    print("1 x", a, "= ", a)
    a += 1


print(" ")
print("No. 4")
    # 7 x 6 = 42
    # 7 x 7 = 49
    # 7 x 8 = 56
    # 7 x 9 = 63
    # 7 x 10 = 70

a = 6
for i in range(5):
    print("7 x", a,"=", 7*a)
    a += 1


print(" ")
print("No. 5")
    # * * * 
    # * * * 
    # * * * 

for i in range(3):
    for j in range(0,3):
        print("*", end=" ")
    print(" ")


print(" ")
print("No. 6")
    # 1 1 1 1
    # 2 2 2 2
    # 3 3 3 3

a = 0
for i in range(3):
    a += 1  
    for j in range(4):
        print(a, end=" ")   
    print(" ")
    

print(" ")
print("No. 7") 
    # (1 1 2 3 5 8 13 21 34 55)
    
k1 = 1
k2 = 1
for i in range(10):
    if i < 2:
        print(1, end= " ")
    else:
        k3 = k1 + k2
        print(k3, end=" ")
        k1 = k2
        k2 = k3

print(" ")
print(" ")
print("No. 8")    
    # (1 2 3 6 11 20 37 68 125 230)

k1 = 1
k2 = 2
k3 = 3

for i in range(1,11):
    if i < 4:
        print(i, end=" ")
    else:
        k4 = k1 + k2 + k3
        print(k4, end= " ")
        k1 = k2
        k2 = k3
        k3 = k4


print(" ")
print(" ")
print("No. 9")
    # 1 1 1 1
    # 1 1 1
    # 1 1
    # 1   
    
for i in range(4):
    for y in range(5,i+1,-1):
        print(1, end=" ")
    print(" ")


print(" ")
print("No. 10")
    # 2 3 2 3 2
    # 3 2 3 2
    # 2 3 2
    # 3 2
    # 2

for i in range(5):
    for y in range(5,i,-1):
        if i % 2 == 0:
            if y % 2 == 1:
                print(2, end= " ")
            else: 
                print(3, end=" ")
        else: 
            if y % 2 == 0:
                print(2, end= " ")
            else: 
                print(3, end=" ")  
    print(" ")  