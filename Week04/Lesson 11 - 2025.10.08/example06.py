"""
What is a Property

- A property allows us to use a method inside a class as if it were an attribute
- In other words, it can be called without parentheses.
- It is commonly used to control reading, writing, and deletion of an attribute
"""


# without Property
class Rectangle:
    def __init__(self, width, height):
        self.width = width  # public value
        self.height = height  # public value

    def area(self):
        return self.width * self.height


calculate_area1 = Rectangle(5, 3)
print(calculate_area1.area())  # 15
# have to use () after functions


# with Property
class Rectangle2:
    def __init__(self, width, height):
        self.width = width  # public value
        self.height = height  # public value

    @property
    def area(self):
        return self.width * self.height


calculate_area2 = Rectangle2(5, 3)
print(calculate_area2.area)  # 15
# no need to use () after functions because of property decorator. It is called as an attribute not a method.
