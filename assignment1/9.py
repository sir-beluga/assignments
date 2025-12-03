total_amount = float(input("Enter the total purchase amount: "))
is_member = input("Are you a member? (True/False): ") == "true"

if total_amount > 1000 and is_member:
 final_amount = total_amount * 0.8
elif total_amount > 1000 and not is_member:
 final_amount = total_amount * 0.9
else:
 final_amount = total_amount

print("Final amount:", final_amount)
