m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100
print("Total marks:", total)
print("Percentage:", percentage)
if percentage > 70:
 grade = "Distinction"
elif percentage > 60:
 grade = "First"
elif percentage > 40:
 grade = "Pass"
else:
 grade = "Fail"
print("Grade:", grade)
