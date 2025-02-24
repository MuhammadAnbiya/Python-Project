name = input("Whos your name ? ")
number = int(input("whats the number ? ")) # 70

if number >= 90: # F
    print(f"{name} Grade A")
elif number >= 80:# F
    print(f"{name} Grade B")
elif number >= 70: # T
    print(f"{name} Grade C")
elif number >= 60:
    print(f"{name} Grade D")
else:
    print(f"{name} Grade E")




