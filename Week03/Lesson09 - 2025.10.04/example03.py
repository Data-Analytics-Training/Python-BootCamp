"""
! Global Scope

x parameter define outside function. It is accessible inside the function


"""

x = 300


def function():
    print("inside function", x)


print("outside function, before function", x)  # 300
function()  # 300
print("outside function, after function", x)  # 300


"""
while in function, defined x value firstly checked in scope of function after than global scope
"""

x = 300


def function2():
    x = 500
    print("inside function2", x)  # 500


print("outside function, before function2", x)  # 300
function2()
print("outside function, after function2", x)  # 300
