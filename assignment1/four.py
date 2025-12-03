current_floor = 5
target_floor = int(input("Enter the floor you want to go to: "))

if target_floor > current_floor:
 print("Lift should go up")
elif target_floor < current_floor:
 print("Lift should go down")
else:
 print("Lift stays at the current floor")
