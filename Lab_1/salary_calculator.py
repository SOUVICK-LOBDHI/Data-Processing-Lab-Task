name = input("Enter name: ")
basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))

gross_salary = basic_salary + allowances

if gross_salary <= 30000:
    tax_percentage = 0
elif gross_salary <= 50000:
    tax_percentage = 5
elif gross_salary <= 80000:
    tax_percentage = 10
else:
    tax_percentage = 15

tax_amount = (gross_salary * tax_percentage)/100
net_salary = gross_salary - tax_amount

print("Name:", name)
print("Gross Salary:", gross_salary)
print("Tax Percentage:", tax_percentage, "%")
print("Tax Amount:", tax_amount)
print("Net Salary:", net_salary)