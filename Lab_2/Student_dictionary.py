student_info = {"Name": input("Enter your name:       "),
                "ID": input("Enter your ID:         "),
                "Department": input("Enter your department: "),
                "CGPA": float(input("Enter your CGPA:       "))
               }
print("\n")
for key, value in student_info.items():
    print(key, " ", value)


if student_info["CGPA"] >= 2.50:
 print("\nGood Standing!")

else:
 print("\nAcademic Warning!")