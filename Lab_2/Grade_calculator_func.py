marks = [float(input("Enter your marks: ")), float(input("Enter your marks: ")), float(input("Enter your marks: ")),float(input("Enter your marks: ")), float(input("Enter your marks: "))]

length = len(marks)
print("Length of marks: ",length)

print("Marks: ",marks)

def calculate_grade(marks):
    total_marks = sum(marks)
    print("Total marks: ", total_marks)

    average_marks = total_marks/length
    print("Average marks: ", average_marks)

    if average_marks >= 80:
          return "A"
    elif average_marks >= 70:
        return "B"
    elif average_marks >= 60:
        return "C"
    elif average_marks >= 50:
        return "D"
    elif average_marks <= 50:
        return "F"
    else:
        print("Your marks are out of range")


grade = calculate_grade(marks)
print("Grade: ", grade)