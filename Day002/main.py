#Prints Welcome Message
print("Welcome to the tip calculator!!")

#Takes bill, tip and no_people input from user
bill = int(input("What is your total bill?: "))
tip = int(input("How much tip would like to give? 10, 12, or 15?: "))
no_people = int(input("How many people to split the bill?: "))

#Calculates the amount payable per person and print the output
bill_per_person = ((tip/100 + 1) * bill)/no_people
print(f"Your bill per person is ${round(bill_per_person,2)}")

#Acknowledgement
print("Thank you for dinning with us!")
