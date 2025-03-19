#take input of a word
string = input ("Please enter a word: ")
#take input of a character
char = input ("Please enter a character: ")
i = 0
count = 0
#loop will to find the occurence of a character
while (i < len(string)): #string operation
  if (string[i]== char): #condition 1
    count = count + 1
  i = i + 1
#display the result
print ("The character", char, "occurs", count, "times in the word", string)