# Variable
Total_bill = None
Percenatge_tip = None
Bill_split = None

# Input
Total_bill = float(input("What is the total bill? $"))
Percenatge_tip = float(
    input("How much percent tip would you like to give? Choose 1% to 100% ")
)
Persons = int(input("How many people to split the bill? "))

# Calculating the tip
tip = (Percenatge_tip / 100) * Total_bill
Total_bill_with_tip = Total_bill + tip
Bill_split_with_tip = Total_bill_with_tip / Persons

print(f"Each person should pay: ${Bill_split_with_tip}")
