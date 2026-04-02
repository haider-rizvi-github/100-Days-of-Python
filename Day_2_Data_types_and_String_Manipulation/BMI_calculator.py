# Variables
Weight = None
Height = None

## Input
Weight = float(input("Enter your weight in Kg: "))
Height = float(input("Enter your height in meter: "))

# Calculating BMI
BMI = Weight / (Height * Height)
print(f"Your BMI is: {BMI}")

if BMI < 25:
    print("Your Weight is in Optimum Range.")
elif BMI < 30:
    print("Your Weight is Overweight.")
elif BMI < 35:
    print("Your Weight is in Obese Class I.")
elif BMI < 40:
    print("Your Weight is in Obese Class II.")
else:
    print("Your Weight is in Obese Class III.")

print(6 + 4 / 2 - (1 * 2))
