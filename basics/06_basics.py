# Improved version of Practice Task for Day 3:
#
# Create a Number Guessing check:
#
# Let Computer Secret Number is 7 (Fix this inn the code)
# Repeatedly ask from user about the Number (Using while loop)
# If Guess is correct then print correct and stop the loop
# If Guess is incorrect then print Try again and ask again

Computer_Secret_number = 7

while True:
    user_number = int(input("Enter The Number: "))
    if user_number == Computer_Secret_number:
        print("Correct")
        break
    else:
        print("Incorrect")
