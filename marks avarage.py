# marks for four subjects
python_marks = float(input("Enter the marks in Python: "))
c_programming_marks = float(input("Enter the marks in C Programming: "))
mathematics_marks = float(input("Enter the marks in Mathematics: "))
physics_marks = float(input("Enter the marks in Physics: "))
total_marks = python_marks + c_programming_marks + mathematics_marks + physics_marks
aggregate = total_marks / 4
if aggregate >= 75:
    grade = "Distinction"
elif 60 <= aggregate < 75:
    grade = "First Division"
elif 50 <= aggregate < 60:
    grade = "Second Division"
elif 40 <= aggregate < 50:
    grade = "Third Division"
else:
    grade = "Fail"
print(f"Total Marks = {total_marks}")
print(f"Aggregate = {aggregate}")
print(f"Grade = {grade}")
