years_of_service = float(input("Enter years of service: "))
salary = float(input("Enter basic salary: "))
if years_of_service > 10:
 bonus = salary * 0.10
elif 6 <= years_of_service <= 10:
 bonus = salary * 0.08
else:
 bonus = salary * 0.05
print("Bonus amount:", bonus)
