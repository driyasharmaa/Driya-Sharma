def mirrored_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
    
# example usage 
rows = int(input("Enter the number of rows: "))
mirrored_triangle(rows)