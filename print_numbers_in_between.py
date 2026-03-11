#Ask user input
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
#Set the condition
start_number = min(first_number, second_number)
end_number = max(first_number, second_number)
for i in range(start_number + 1, end_number):
    print(i)