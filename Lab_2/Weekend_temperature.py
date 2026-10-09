temperatures = (
    (70, 75, 72), #Saturday
    (68, 71, 69)  #Sunday
)

days = ("Saturday", "Sunday")
times = ("Morning", "Afternoon", "Evening")

#Use a for loop for each temperature
for i, day_temps in enumerate(temperatures): #enumerate() used for read both index and values
    for j, temp in enumerate(day_temps):
        print(f"{days[i]} {times[j]}: {temp}")

# Calculate the highest and lowest temperature in the tuple
flat_temperatures = [temp for day_temps in temperatures for temp in day_temps]

print("\nFlat Temperatures: ", flat_temperatures)
highest_temp = max(flat_temperatures)
lowest_temp = min(flat_temperatures)

print(f"\nHighest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")