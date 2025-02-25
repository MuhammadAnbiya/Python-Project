rows = 5

# Upper Triangle
k = 2 * rows - 2

# Outer loop to handle number of rows
for i in range(rows):
    
    #Inner loop to handle number of spaces
    for j in range(k):
        print(end=" ")
    k = k - 1
    
    #Inner loop to print patterns
    for j in range(0, i + 1):
        print(i+1, end=" ")
    print("")

    
# Lower Triangle   
k = rows - 2

# Outer loop to handle number of rows
for i in range(rows, -1, -1):
    
    #Inner loop to handle number of spaces
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    
    #Inner loop to print patterns
    for j in range(0, i + 1):
        print(i+1, end=" ")
    print("")
