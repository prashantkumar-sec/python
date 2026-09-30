# 1. Basics + Operators :
#
# Make a Simple calculator
# Take two numbers input from user and one operator (+, -, *, /)
# Print Result using f-string
# Print invalid message when wrong operator entered

print("----------------------------------------")
print("------CALCULATOR FOR TWO NUMBERS--------")
print("----------------------------------------")

num1 ,num2 = map(int ,input("Enter 1st Number & 2nd Number").split())
operation = int(input("Enter 1.addition(+) 2.subtraction(-) 3.multiplication(*) 4.division(/): "))
if operation == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == 3:
    print(f"{num1} X {num2} = {num1 * num2}")
elif operation == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Choose a valid operator")
