# Take input of number of units consumed from the user
units = int(input("Please enter the number of units you consumed: "))
#Check condition of units consumed
#Then calculate mount and surcharge accordingly
#Surcharge is the tax value
#Check for units less than 50
if(units<50):
    amount = units*2.60

#check for units less than 100
elif(units<=100):
    amount = 130 + ((units - 50)*3.25)

#check for units for less than or equal to 200
elif (units<=200):
    amount = 130 +162.50 + ((units - 100)*5.26)
    surcharge = 45

#check for all the cases other than mentioned
#when units cosumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200)*8.45)
    surcharge = 75

#calculate and display the total electricity bill
#total amount = amount + surcharge
total = amount + surcharge
print ("\nElectricity Bill = %.2f" %total)