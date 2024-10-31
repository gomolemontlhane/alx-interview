#!/usr/bin/python3
"""
Main file for testing the validUTF8 function
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# Test cases
data1 = [65]  # Expected output: True (valid ASCII character)
print(validUTF8(data1))

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# Expected output: True (valid sequence of ASCII characters)
print(validUTF8(data2))

data3 = [229, 65, 127, 256]  # Expected(contains an invalid byte)
print(validUTF8(data3))

data4 = [197, 130, 1]  # Expected output: Tcharacter followed by 1-byte)
print(validUTF8(data4))
