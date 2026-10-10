meal = input("Enter food name: ")
drink = input("Enter drink name: ")

if meal == "pizza" and drink == "cola":
    print("Valid order")
    print("Bon appetite! Enjoy your meal!")
else:
    print(f"{meal} - {drink} is not valid order")
