meal = input("Enter food name: ")
drink = input("Enter drink name: ")

# Let's elaborate on our questions further
if meal == "pizza" and (drink == "cola" or drink == "ayran"):
    print("Valid order")
    print("Bon appetite! Enjoy your meal!")
else:
    print(f"{meal} - {drink} is not valid order")
