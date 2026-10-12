"""Demonstrates recursive function to calculate factorial of a number."""


def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)


print(calculate_factorial(5))  # 120
print(calculate_factorial(15))  # 1307674368000
print(calculate_factorial(1559))
# Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
