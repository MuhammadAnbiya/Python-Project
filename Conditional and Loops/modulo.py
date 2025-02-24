def main():
    num = int(input("whats the number ?"))
    if is_genap(num):
        print("genap")
    else:
        print("ganjil")

def is_genap(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()