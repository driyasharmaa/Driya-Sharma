#take input
print("Mirrored right angle triangle pattern of stars (*)")
n = int(input("Enter the number of rows: "))
#outer loop to handle number of rows
for i in range (1, n + 1):
    #print spaces first
    for j in range (n - 1):
        print(" ", end = "")
    #then print stars
    for k in range (i):
        print ("*", end = "")
    #new line after each row
    print()