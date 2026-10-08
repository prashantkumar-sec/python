# Practice Task: OOP Part 2 (Encapsulation, Dunder Methods, classmethod)
#
# 2.Encapsulation: _protected aur __private
#
class Device:
    def __init__(self,name, ip):
        self.name=name
        self._ip=ip  # convention: "don't tamper with inner things from outside"
        self.__password = "admin"   # name mangling, harder to access
