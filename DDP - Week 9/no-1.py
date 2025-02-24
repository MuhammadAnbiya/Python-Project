# arr = [12, 45, 78, 23, 56, 91, 34]

# urutkan dari yang terbesar ke terkecil, setelah itu print element yang terbesar dan terkecilnya, gunakan array method untuk menyelesaikannya ya

arr = [12, 45, 78, 23, 56, 91, 34]

urut = sorted(arr)
print(f"terkecil", urut[0], "terbesar", urut[len(arr)-1])