earth_weight = float(input("Enter your Earth weight: "))
planet = int(input("Enter planet number (1-7): "))

if planet == 1:
 weight = earth_weight * 0.38
elif planet == 2:
 weight = earth_weight * 0.91
elif planet == 3:
 weight = earth_weight * 0.38
elif planet == 4:
 weight = earth_weight * 2.53
elif planet == 5:
 weight = earth_weight * 1.07
elif planet == 6:
 weight = earth_weight * 0.89
elif planet == 7:
 weight = earth_weight * 1.14
else:
 weight = None

if weight is not None:
 print("Your weight on the selected planet is:", weight)
else:
 print("Invalid planet number")