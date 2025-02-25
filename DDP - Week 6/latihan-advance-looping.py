print("No.1")
print("1 2 3 6 11 20 37 68 125 230")

a = 1
b = 2
c = 3

for i in range(10):
    if i==0 or i==1 or i==2:
        print(i+1, end= " ")
    else:
        d = a+b+c
        print(d, end=" ")
        a = b
        b = c
        c = d


    # No. 2
# row = 3
# col = 4

# for i in range(row):
#     for j in range(col):
#         print(i+1,end=" ")
#     print( )
    
    #no 3
# row = 3
# col = 4

# for i in range(row):
#     for j in range(col):
#         print(j+1,end=" ")
#     print( )
    
    #no. 4
# row = 3
# col = 4

# for i in range(row):
#     for j in range(col):
#         print(j+1+i,end=" ")
#     print( )

    # No. 5
# for i in range(5):
#     for j in range(5):
#         print(j+1, end=" ")
        
#     print()
    
    
    #No.1
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25    


# for i in range(5):
#     b = 0
#     for j in range(5):
#         print(i+1+b, end=" ")
#         b += i+1
#     print()


    # No.2
# 1 
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

# for i in range(5):
#     for j in range(0,i+1):
#         print(j+1, end=" ")
#     print()
    
    
    # No.3
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

# for i in range(5):
#     for j in range(i+1,6):
#         print(j, end=" ")
#     print()


    #No.4
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

# for i in range(5):
#     for j in range(5):
#         print((i+1)*(j+1), end=" ")
#     print()


    #No.5
# 1 3 5 7 9
# 2 4 6 8 10
# 3 5 7 9 11
# 4 6 8 10 12
# 5 7 9 11 13

# for i in range(5):
#     for j in range(5):
#         print(i+1, end=" ")
#         i += 2
#     print()

    #No.6
# + + + + 5
# + + + 4 5
# + + 3 4 5
# + 2 3 4 5
# 1 2 3 4 5

# row = 5
# col = 5

# for i in range(row):
#     for j in range(col):
#         if j < col-(i+1):
#             print("+", end=" ")
#         else:
#             print(j+1, end= " ")
#     print()
    
    #No.7
# A B A B A
# B A B A B
# A B A B A
# B A B A B

# for i in range(4):
#     for j in range(5):
#         if i % 2 == 0:
#             if j % 2 == 0:
#                 print("A", end= " ")
#             else:
#                 print("B", end=" ")
#         else:
#             if j % 2 == 1:
#                 print("A", end= " ")
#             else:
#                 print("B", end=" ")
#     print()
    

    #No. 8
# S O S O S
# O S O S
# S O S
# O S
# S

# for i in range(5):
#     for j in range(i+1,6):
#         if i % 2 == 0:
#             if j % 2 == 0:
#                 print("O", end= " ")
#             else:
#                 print("S", end=" ")
#         else:
#             if j % 2 == 1:
#                 print("S", end= " ")
#             else:
#                 print("O", end=" ")
#     print()


    #No.9
# len = int(input("panjang fibonaci nya : "))
# a = 1
# b = 1
# c = 1
# for i in range(1, len+1):
#     if i < 3:
#         print("*" * c, end=" ")
#     else:
#         c = a + b
#         print("*" * c, end= " ")
#         a = b
#         b = c
#     print()





 