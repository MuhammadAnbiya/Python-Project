x = input("=") 
for i in range(0,len(x)):
    for j in range(0,len(x)):
        print(x[j], end=" ") if j <i+1  else print("*", end=" ")
    print()

