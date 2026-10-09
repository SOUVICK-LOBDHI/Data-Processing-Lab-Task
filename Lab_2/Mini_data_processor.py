# Create a list of dictionaries for 5 students.
# Each student should have a name, department, marks, and attendance.
# Write functions to: (1) calculate the average marks, (2) find the student with the highest marks,
# and (3) count students with attendance below 80%. Use for loops inside your functions.
# Finally, print a short summary of the results.

students = [
    {"name": input("Student name: "), "marks": float(input("Student marks: ")), "attendence": float(input("Student attendence: "))},
    {"name": input("Student name: "), "marks": float(input("Student marks: ")), "attendence": float(input("Student attendence: "))},
    {"name": input("Student name: "), "marks": float(input("Student marks: ")), "attendence": float(input("Student attendence: "))},
    {"name": input("Student name: "), "marks": float(input("Student marks: ")), "attendence": float(input("Student attendence: "))},
    {"name": input("Student name: "), "marks": float(input("Student marks: ")), "attendence": float(input("Student attendence: "))}
]

#1. calculate average marks
def average_marks(students):
    total_marks = 0
    for student in students:
        total_marks += student["marks"]
    return total_marks / len(students)

#2. calculate highest marks
def highest_marks(students):
    highest_marks = students[0]
    for student in students:
        if student["marks"] > highest_marks["marks"]:
            highest_marks = student
    return highest_marks

#3. Student attendence below 80%
def calculate_attendence(students):
    attendence = 0
    for student in students:
       if student["attendence"] < 80:
           attendence += 1
    return attendence

average = average_marks(students)
highest = highest_marks(students)
attendence = calculate_attendence(students)

print("\nAverage marks: ", average)
print("Highest Students Name: ", highest["name"])
print("Highest marks: ", highest["marks"])
print("Attendance: ", attendence)


