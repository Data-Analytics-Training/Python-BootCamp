"""
Operation related to string
"""

name = "RidvanCelikbas"

length = len(name)
print(length)

print(name[0])  # R
print(name[13])  # s

# left to right =>  0,   1,   2,   3,   4,   5,  6,  7,  8,  9, 10, 11, 12, 13
# right to left => -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
print(name[-1])  # s
print(name[-14])  # R


# slicing
# print(name[starting index: ending index])
print(name[0:6])  # Ridvan
print(name[6:])  # Celikbas
print(name[:6])  # Ridvan
print(name[:])  # RidvanCelikbas

# print(name[starting index: ending index: step])
print(name[0:14:2])  # Riaelksb
print(name[0:14:3])  # Rveia
print(name[0:6:2])  # Rda
print(name[-10:-4:2])  # aCl
print(name[5::2])  # neibs

# Searching in string
print("R" in name)  # True
print("K" in name)  # False
print("lik" in name)  # True

# String methods
print(name.upper())  # to upper case => RIDVANCELIKBAS
print(name.lower())  # to lower case => ridvancelikbas
print(name.capitalize())  # to capitalise first letter of each word =>  Ridvan celikbas
print(name.isalnum())  # is alphanumeric => True
print(name.isdigit())  # is digit => False
