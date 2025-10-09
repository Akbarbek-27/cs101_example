name = input("Student name: ")
grade = float(input("GPA from (0.0-4.5):"))
credits = int(input("Total credit hours: "))
require_grade = grade >= 3.5
require_credits = credits >= 12
requirements = require_grade and require_credits
gpa_difference = float(3.5 - grade)
credits_difference = int(12 - credits)
print(f"Student information: {name,grade,credits}")
print(f"Whether you made the dean’s list:{requirements}")
print(f"How many more GPA points needed: {gpa_difference}" if grade <= 3.5 else '' )
print(f"How many more credits needed:  {credits_difference}" if credits <= 12 else '')
