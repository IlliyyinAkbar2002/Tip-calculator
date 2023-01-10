print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")

# Convert to floating 
convert_bill = float(bill)

input_tip = input("How much tip would you like to give? 10, 12, or 15?")

# Convert to integer
convert_tip = int(input_tip)

person_tip = input("How many people to split the bill? ")

# convert to integer
convert_person = int(person_tip)

# Calculate the total bill

tip_1 = 10
tip_2 = 12
tip_3 = 15

formula_tip = (convert_bill * tip_1 * convert_tip) + (convert_bill * tip_2 *
                                                      convert_tip) + (convert_bill * tip_3 * convert_tip) // convert_person

print(f"Each person should pay: {formula_tip}")
