#Take input for the student that he can attend the exam or nit
medical_cause=input("Did you have a medical cause yes or no: ")
#Take input of the attendance 
atten = int(input("Enter the students attendance: "))
#checking the user input predicting output accordingly
if medical_cause == 'Y' : #checking the condition 1 
    print("You are allowed.")
else:
    if atten>=75: #checking the condition 2
        print ("Allowed")
    else:
        print("Not allowed")