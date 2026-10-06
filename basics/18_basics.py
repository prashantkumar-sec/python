# Practice Task: Network Device Inventory (Inheritance & Polymorphism)
#
# Requirements:
#
# Create a parent class Device with:
# Attributes: name, ip
# Method info() that prints the basic details
# Method to_dict() that returns the object's data as a dictionary
# Create a child class Router(Device):
# Extra attribute: protocol (e.g., OSPF, BGP)
# Use super().__init__() to reuse the parent's setup
# Override info() to also show the protocol
# Override to_dict() to include protocol
# Create a child class Switch(Device):
# Extra attribute: ports (number of ports)
# Override info() and to_dict() the same way
# Build an inventory list containing at least 2 routers and 2 switches.
# Loop through the inventory and call info() on each device (polymorphism in action).
# Use isinstance() to count how many routers and how many switches are in the inventory, and print the counts.
#
import json


class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def info(self):
        print(f"The Name of The Device is {self.name} and ip of the device is {self.ip}")

    def to_dict(self):
        return {"name": self.name, "ip": self.ip}

class Router (Device):
    def __init__(self, name, ip, protocol):
        super().__init__(name,ip)
        self.protocol = protocol

    def info(self):
        print(f"The Name of The Device is {self.name} and ip of the device is {self.ip} using Protocol {self.protocol}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Router"
        data["protocol"] = self.protocol
        return data

class Switch(Device):
    def __init__(self, name, ip, ports):
        super().__init__(name,ip)
        self.ports = ports

    def info(self):
        print(f"The Name of The Device is {self.name} and ip of the device is {self.ip} using Ports {self.ports}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Switch"
        data["ports"] = self.ports
        return data


inventory = [
    Router("R1", "10.0.0.1", "OSPF"),
    Router("R2", "10.0.0.2", "BGP"),
    Switch("SW1", "10.0.1.1", 24),
    Switch("SW2", "10.0.1.2", 48),
]


def save_inventory(inventory, filename):
    data = [d.to_dict() for d in inventory]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


with open("inventory.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))
print(data[0]["type"])

for device in inventory:
    device.info()

routers = sum(1 for d in inventory if isinstance(d, Router))
switches = sum(1 for d in inventory if isinstance(d, Switch))

save_inventory(inventory,"inventory.json")
print(f"Routers: {routers}")
print(f"Switches: {switches}")