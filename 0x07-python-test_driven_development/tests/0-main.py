#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(4, 5))
print(add_integer(-100, 6))
print(add_integer(3))
print(add_integer(32.4, -7))
try:
    print(add_integer(5, "Martin"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
