#Set the range for 10 automatic input function
#Assign Variables
for i in range (1, 11):
    user_input = float(input("Enter number {}: ".format(i)))
    if user_input in range(2, 11):
        user_input -= user_input
print(user_input)


#Set the conditions