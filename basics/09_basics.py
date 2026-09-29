#Step-1: Basic Function

def greet():
    print("Hello,Viewer")

greet() #call is necessary otherwise nothing will be happened

#step-2: Parameters input

def greet(name):
    print(f"Hello, {name}")

name = input("Enter Your Name: ")
greet(name)

#step-3: Return

def add(a,b):
    return a + b
result = add(2,3)
print(result)

#step-4: Default parameters

def greet(name ,greeting="Good morning"):
    return f"{name} {greeting}"
print(greet("Prashant"))
print(greet("Shree", "Namaste"))

# One function one use

def is_even(n):
    return n % 2 == 0