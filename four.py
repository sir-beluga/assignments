# Take marks (0–100) and print “Pass” if ≥40, else “fail

marks=int(input("enter your marks "))
if  marks>100 or marks<0:
    print("invalid")
elif marks>=40:
    print("pass")
else:
    print("fail")