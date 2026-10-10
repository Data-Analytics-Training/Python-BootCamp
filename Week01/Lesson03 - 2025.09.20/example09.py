"""
Calculate to multiply numbers entered by the user until they enter 0
"""

multiply = 1

while True:
    number = int(input("Please enter a number to multiply: \n(to exit enter 0) "))
    if number == 0:
        break
    multiply *= number

print(f"The multiplication of all numbers is {multiply}")

# Another way
multiply = 1
while True:
    number = int(input("Please enter a number to multiply: \n(to exit enter 0) "))
    if not (number == 0):  # if number != 0
        multiply *= number
    else:
        print(f"The multiplication of all numbers is {multiply}")
        break
