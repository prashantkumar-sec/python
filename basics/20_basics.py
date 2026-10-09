# Practice Task: OOP Part 2 (Encapsulation, Dunder Methods, classmethod)

class Device:
    # 4. __init__
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip                    # setter call hoga, direct save nahi
        self.__password = "admin"       # name mangling, harder to access

    # 2. Encapsulation: getter
    @property
    def ip(self):
        return self._ip                 # convention: "don't tamper with inner things from outside"

    # 3. Setter
    @ip.setter
    def ip(self, value):
        parts = value.split(".")
        if len(parts) != 4:
            raise ValueError("IP mein 4 parts hone chahiye")
        self._ip = value                # raise ke baad, if ke bahar

    def __str__(self):
        return f"{self.name} ({self.ip})"       # print(d) ke liye, human friendly

    def __repr__(self):                         # debugging ke liye, developer friendly
        return f"Device(name={self.name!r}, ip={self.ip!r})"


d = Device("R1", "192.168.1.1")
print(d)        # R1 (192.168.1.1)
print([d])      # [Device(name='R1', ip='192.168.1.1')]
print(d.ip)     # 192.168.1.1

d.ip = "10.0.0.5"
print(d.ip)     # 10.0.0.5

d.ip = "hello"  # ValueError aayega, expected hai