#Set the range for 10 automatic input function
#Assign Variables
#Set the conditions
first_number = float(input("Enter a number: "))
for i in range (9):
    remaining_numbers = float(input("Enter a number: "))
    first_number -= remaining_numbers
print(first_number)