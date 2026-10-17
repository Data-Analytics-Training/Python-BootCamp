import re


class Rectangle:
    def __init__(self, width, height):
        self._width = width  # private value
        self._height = height  # private height

    @property  # get getter
    def width(self):
        return self._width

    @width.deleter  # deleter
    def width(self):
        print("Deleting width")
        del self._width


rect = Rectangle(5, 3)
del rect.width  # delete width
