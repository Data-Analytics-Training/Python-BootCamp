"""
Write a code to check if a given number is an Armstrong number or not.
"""

#  * First method
number = int(input("Please enter a number: "))
string_number = str(number)
power = len(string_number)
sum = 0

for dd in string_number:
    sum = sum + int(dd) ** power
    print(dd, sum)

if sum == number:
    print(f"{number} is a Armstrong number.")
else:
    print(f"{number} is not an Armstrong number")


# * Second method (checking all numbers from 1 to 10000)
for number in range(1, 10000):
    string_number = str(number)
    power = len(string_number)
    sum_ = 0

    for dd in string_number:
        sum_ = sum_ + int(dd) ** power
    if sum_ == number:
        print(f"{number} is an Armstrong number")
