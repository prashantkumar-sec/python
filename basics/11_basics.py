# File Handling + Exception Handling

# Step-1: Writing a File
with open ("notes.txt", "w") as f:
    f.write("Hello I am Prashant Kumar\n")
    f.write("Learning Python\n")

# Step-2: Reading a File
with open("notes.txt","r") as f:
    content = f.read() # whole file at once
    print(content)

with open("notes.txt","r") as f:
    for line in f:
        print(line.strip()) # By using strip() extra \n will be removed

# Step-3: Exceptions (try / except)

try :
    with open("missing.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist")

# What if a user entered text in the place of number
try:
    age = int( input("Age: "))
except ValueError:
    print("Enter a number")
