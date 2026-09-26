# ask user for their username and their password
# if username is "admin" AND password "secure123" print access granted
# if username is correct but password is incorrect then print wrong password
# if both are incorrect print access denied

user_name = input("Enter your Username: ")
user_passwd = input("Enter your Password: ")

if user_name == "admin" and user_passwd == "secure123" :
    print("Access Granted")
elif user_name == "admin":
    print("wrong Password")
else :
    print("Access Denied")