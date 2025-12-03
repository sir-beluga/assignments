marks = int(input("Enter the student's marks (0–100): "))
if 90 <= marks <= 100:
    grade = "A+"
elif 80 <= marks <= 89:
    grade = "A"
elif 70 <= marks <= 79:
    grade = "B+"
elif 60 <= marks <= 69:
    grade = "B"
elif 50 <= marks <= 59:
    grade = "C"
elif 40 <= marks <= 49:
    grade = "D"
elif 0 <= marks < 40:
    grade = "E"
else:
    grade = "Invalid marks"
print("Grade:", grade)
