birth_year = int(input("What is your birth year? "))

age = 2026 - birth_year

if age >= 18:
    print("You can obtain a driver license")
else:
    print("You can not get driver license")
    print(18 - age, "years later you will be able to obtain a driver license.")
    print(
        f"You are {age} years old. You have {18 - age} years left until you can obtain a driver license."
    )
