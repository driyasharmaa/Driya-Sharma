#take input
print ("Half pyramid pattern of stars (*):")
n = int(input("Enter the number of rows"))
#outer loop to handle number of columns
for i in range (n):
    #inner loop to handle number of columns 
    for j in range(i+1):
    #display result
        print("* ", end = "")
    print ()