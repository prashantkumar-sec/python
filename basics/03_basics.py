# write a small script:

# ask user for their name and age
# greet the user
# tell the user their age in 2030
user_name = input("Enter your name: ")
user_age = int( input ("Enter your age: "))

print("Hello "+user_name)
future_age_in = 10

user_age_2030 = user_age + future_age_in

print(f"your age will be {user_age_2030} in 2030")