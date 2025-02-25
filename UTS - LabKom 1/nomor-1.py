name = "nugraha"

for i in range(len(name)):
    for j in range(len(name)):
        if len(name)-j > i:
            print(name[j].capitalize(), end=" ")
        else:
            print("*", end= " ")
    print()