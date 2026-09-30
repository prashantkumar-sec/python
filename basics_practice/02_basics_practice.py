
user_marks = int(input("Enter your Marks (0-100):  "))

if user_marks >= 90:
    print(f"The grade of {user_marks} is A.")
elif user_marks >=75 or user_marks <=89:
    print(f"The grade of {user_marks} is B.")
elif user_marks >=60 or user_marks<=74 :
    print(f"The grade of {user_marks} is C.")
elif user_marks <60:
    print(f"The grade of {user_marks} is Fail.")
else:
    print("marks is not in range 0-100")
