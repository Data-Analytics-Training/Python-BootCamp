road = float(input("Enter the road length in km: "))
time = float(input("Enter the time taken to travel the road in hours: "))
speed = road / time

if speed > 120:
    print(f"Your speed is {speed} km/h.")
    print("You are exceeding the speed limit")
else:
    print(f"Your speed is {speed}")
    print("Thank you for driving safely.")
