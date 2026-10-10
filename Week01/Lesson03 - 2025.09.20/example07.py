"""
While loop with user input
"""

answer = input("Do you want pizza? (yes/no) ")

while answer.lower() == "yes":
    print("Here is your pizza, Bon Appetit")
    answer = input("Do you want one more? (yes/no) ")

# Another way to do it
answer = bool(input("Do you want pizza? "))
while answer:  # while answer== True:
    print("Here is your pizza, Bon Appetit")
    answer = bool(input("Do you want one more? "))
