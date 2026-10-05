class Contact:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        print(f"{self.name} ---> {self.phone}")

print(Contact("Prashant","839953"))