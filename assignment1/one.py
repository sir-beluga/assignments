a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
 print("All numbers are equal")
elif a == b or b == c or a == c:
 print("Two numbers are equal")
else:
 print("All numbers are different")