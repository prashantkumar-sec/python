# Write a Python program that takes an integer from the user and:

# 1. Checks whether the number is **positive, negative, or zero**.
# 2. Checks whether the number is **even or odd** (only if it's not zero).
# 3. Calculates the **sum of its digits**.
# 4. Reverses the number


num = int(input("Enter an integer: "))

# 1. Positive, negative or zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Even or odd (only if not zero)
if num != 0:
    print("Even" if num % 2 == 0 else "Odd")

# 3 & 4. Sum of digits and reverse in a single loop
temp = abs(num)
digit_sum = 0
reverse = 0

while temp:
    digit = temp % 10
    digit_sum += digit
    reverse = reverse * 10 + digit
    temp //= 10

print("Sum of digits:", digit_sum)

if num < 0:
    reverse = -reverse

print("Reversed number:", reverse)
