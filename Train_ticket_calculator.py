name = input("Enter passenger name: ")
destination = input("Enter destination(Chittagong/Sylhet/Khulna/Faridpur/Cox's Bazar): ")
email = input("Enter email address: ")
ptype = input("Enter passenger type(Adult/Child/Student/Senior): ")
tickets = int(input("Enter number of tickets: "))

# lower() diye small letter banano, strip() diye age-pore-er space fela
dest = destination.strip().lower()
pt = ptype.strip().lower()

if dest == "chittagong":
    fare = 550
    dest_name = "Chittagong"
elif dest == "sylhet":
    fare = 500
    dest_name = "Sylhet"
elif dest == "khulna":
    fare = 450
    dest_name = "Khulna"
elif dest == "faridpur":
    fare = 300
    dest_name = "Faridpur"
elif dest == "cox's bazar":
    fare = 695
    dest_name = "Cox's Bazar"
else:
    fare = 0
    dest_name = destination
    print("Invalid destination entered.")

if pt == "adult":
    discount = 0
    type_name = "Adult"
elif pt == "child":
    discount = 50
    type_name = "Child"
elif pt == "student":
    discount = 40
    type_name = "Student"
elif pt == "senior":
    discount = 30
    type_name = "Senior"
else:
    discount = 0
    type_name = ptype
    print("Invalid passenger type entered.")

total_fare = fare * tickets
total_fare = total_fare - (total_fare * discount) / 100

print("BANGLADESH RAILWAY TICKET")
print("Passenger Name:", name)
print("Email Address:", email)
print("Destination:", dest_name)
print("Passenger Type:", type_name)
print("Tickets:", tickets)
print("Discount:", discount, "%")
print("Total Fare:", total_fare)