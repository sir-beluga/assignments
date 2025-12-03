age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
days = int(input("Enter number of days worked: "))
if 18 <= age < 30:
 if gender == "M":
  wage_per_day = 700
elif gender == "F":
 wage_per_day = 750
elif 30 <= age <= 40:
 if gender == "M":
  wage_per_day = 800
elif gender == "F":
 wage_per_day = 850
else:
 wage_per_day = 0
total_wage = wage_per_day * days
print("Total wage:", total_wage)
