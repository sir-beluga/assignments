age = int(input("Enter your age: "))
if age >= 18:
    has_degree = input("Do you have a degree? (Yes/No): ").lower()
    if has_degree == "yes":
        experience = float(input("Enter years of work experience: "))
        if experience > 3:
            print("Highly Eligible.")
        elif 1 <= experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("Not eligible due to lack of degree.")
else:
    print("Not eligible due to age.")
