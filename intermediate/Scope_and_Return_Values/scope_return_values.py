def check():
    result = "ok"       # local: Only inside function

check()
# print(result)       # NameError

def add(a, b):
    print(a + b)    # It just shows, returns None

def add2(a, b):
    return a + b    # returns the value

x = add2(2, 3) * 10     # 50

def is_adult(age):
    if age < 0:
        return False    # wrong input, stopped right here
    return age >= 18
#
# Today's task
#
# validate_port(port) should return True or False:
#
# The port should be an integer (a string like "80" is also fine, so convert it to int).
# Range is 1 to 65535.
# Wrong input (like "abc") should not crash, return False instead (hint: try/except).
#
def validate_port(port):
    try:
        port = int(port)
    except (ValueError, TypeError):
        return False
    return 1 <= port <= 65535

port_tests = [(80, True), ("443", True), (0, False),
         (65535, True), (65536, False), ("abc", False)]
for value, expected in port_tests:
    got = validate_port(value)
    print(value, "->", got, "PASS" if got == expected else "FAIL")

# is_private_ip(ip) returns True or False:
#
# ip.split(".") should give 4 parts, each part a number between 0 and 255.
# Private ranges:
# 10.0.0.0 – 10.255.255.255
# 172.16.0.0 – 172.31.255.255
# 192.168.0.0 – 192.168.255.255
# Returns False for invalid IPs.

def is_private_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False

    nums =[]
    for p in parts:
        try:
            n = int(p)
        except ValueError:
            return False
        if n < 0 or n > 255:
            return False
        nums.append(n)

    a, b = nums[0], nums[1]
    return  (a == 10
            or (a == 172 and 16 <= b <= 31)
            or (a == 192 and b == 168))

ip_tests = [("192.168.1.10", True), ("10.0.0.5", True), ("172.16.5.1", True),
         ("172.32.0.1", False), ("8.8.8.8", False), ("192.168.1", False)]
for value, expected in ip_tests:
    got = is_private_ip(value)
    print(value, "->", got, "PASS" if got == expected else "FAIL")