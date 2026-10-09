marks = [float(input("Enter mark for Data Processing: ")), float(input("Enter mark for Intro to Data Science: ")), float(input("Enter mark for Programming for Data Science: ")), float(input("Enter mark for Python: ")), float(input("Enter mark for Data Mining: "))]

print(len(marks))
print("Marks for each subject:", marks)


def grade_calculator(marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    print("Total marks: ", total_marks)
    print("Average marks: ", average_marks)
    highest_mark = max(marks)
    lowest_grades = min(marks)
    print("Highest mark: ", highest_mark)
    print("Lowest mark: ", lowest_grades) 

    passed_courses = sum(1 for mark in marks if mark >= 50)
    failed_courses = sum(1 for mark in marks if mark < 50)
    print("Number of courses passed: ", passed_courses)
    print("Number of courses failed: ", failed_courses)

    if average_marks >= 90:
        print("Grade: A+")
    elif average_marks >= 85:
        print("Grade: A")
    elif average_marks >= 80:
        print("Grade: B+")
    elif average_marks >= 75:
        print("Grade: B")
    elif average_marks >= 70:
        print("Grade: C+")
    elif average_marks >= 65:
        print("Grade: C")
    elif average_marks >= 60:
        print("Grade: D+")
    elif average_marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")

grade_calculator(marks)