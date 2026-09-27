# Practice Task for Day 3:
#
# Create a Number Guessing check:
#
# Let Computer Secret Number is 7 (Fix this inn the code)
# Repeatedly ask from user about the Number (Using while loop)
# If Guess is correct then print correct and stop the loop
# If Guess is incorrect then print Try again and ask again

Computer_Secret_number = 7

user_number = int ( input("Please enter the number: "))

while user_number != Computer_Secret_number :
    user_number = int ( input("Try again: "))
    continue
if user_number == Computer_Secret_number :
    print("correct")






