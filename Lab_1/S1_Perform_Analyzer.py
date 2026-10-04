name = input("Enter your name: ")

total_marks = 0
passed = 0
highest_marks = 0
lowest_marks = 100

for i in range(1,6):
    course_marks = float(input("Enter course marks: "))
    
    total_marks += course_marks

    if course_marks >= highest_marks: 
     highest_marks = course_marks

    if course_marks <= lowest_marks:
     lowest_marks = course_marks

    if course_marks >= 50:
     passed += 1

average_marks = total_marks / 5

if average_marks >= 80:
    result = "Excellent"
elif average_marks >= 70:
    result = "Good"
elif average_marks >= 60:
    result = "Satisfactory"
elif average_marks >= 50:
    result = "Pass"
else:
    result = "Needs Improvement"

print("Name:", name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Number of Passed Courses:", passed)
print("Result:",result)
      