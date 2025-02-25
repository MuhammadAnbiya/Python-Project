name = input("=")

for i in range(len(name)):
    for j in range(len(name)):
        if len(name) % 2 == 1:
            if i == int((len(name)+1)/2)-1:
                print(name[j].capitalize(),end=" ")
            else:
                if j == int((len(name)+1)/2)-1:
                    print(name[i].capitalize(),end=" ")
                else:
                    print("*",end=" ")
        else:
            if i == int(len(name)/2):
                print(name[j].capitalize(),end=" ")
            else:
                if j == int(len(name)/2):
                    print(name[i].capitalize(),end=" ")
                else:
                    print("*",end=" ")
    print() 
