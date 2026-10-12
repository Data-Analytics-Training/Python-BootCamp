"""Uses recursion to reverse a string."""


def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        # return string[-1] + reverse_string(string[0 : len(string) - 1])
        # return string[-1] + reverse_string(string[:-1])
        return reverse_string(string[1:]) + string[0]


print(reverse_string("Hello World!"))
