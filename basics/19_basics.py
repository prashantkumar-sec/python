# Practice Task: OOP Part 2 (Encapsulation, Dunder Methods, classmethod)
# 1. __str__ OR __repr__
class Device:
    def __init__(self, name,ip):
        self.name = name
        self.ip = ip

    def __str__(self):
        return f"{self.name} ({self.ip})"   # for print(d), human friendly

    def __repr__(self):             # for debugging, Developer Friendly
        return f"Device (name={self.name!r}, ip={self.ip!r})"

d = Device("R1","192.168.1.1")
print(d)        # R1 (192.168.1.1)
print([d])      # [Device (name='R1', ip='192.168.1.1')]