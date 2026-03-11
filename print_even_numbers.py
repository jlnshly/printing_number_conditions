#Set range
#Name variables
even_numbers = 0
for i in range(1, 11):
    user_input = float(input(f"Enter a number: "))
    if float(user_input) % 2 == 0:
        even_numbers += 1
print(even_numbers)