# Classes & Objects (OOP basics):
#
class Contact:
    def __init__ (self, name, phone):
        self.name = name #attribute
        self.phone = phone #attribute

    def show(self):    #method
        print(f"{self.name}--> {self.phone}")

c1 = Contact("Shree","7287246292")
c2 = Contact("Prashant","8093820423")
c1.show()
c2.show()