meal = input("Enter food name: ")
drink = input("Enter drink name: ")

# Let's elaborate on our questions further
if meal == "pizza":
    print("Pizza is a valid meal order.")
    if drink == "cola" or drink == "ayran":
        print("Valid order")
        print("Bon appetite! Enjoy your meal!")
    else:
        print(f"{drink} can be returned")
else:
    print(f"{meal} is not valid order")
