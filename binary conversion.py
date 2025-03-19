# function to convert decimal to binary 
def decimal_to_binary (n):
    return bin (n).replace("0b", "")
#taking user input
decimal_number = int(input("Enter a decimal number: "))
#converting to binary
binary_number = decimal_to_binary(decimal_number)
#displaying the result
print(f"Binary equivalent of {decimal_number} is {binary_number}")