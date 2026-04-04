# variables
ticket_price = None


print("Welcome to Rollercoaster ticketing system!")
age = int(input("What is your age? "))
height = int(input("What is your height in cm? "))

# calculation
if height >= 120 and age > 5:
    if age > 5 and age < 12:
        ticket_price = 10
    elif age >= 12 and age < 18:
        ticket_price = 15
    elif age >= 18 and age < 65:
        ticket_price = 20

    Photographs = input("Do you want a photograph taken? Y or N. ")
    if Photographs == "Y" or Photographs == "y":
        ticket_price += 3
        print(f"Your final ticket price is ${ticket_price}.")
    else:
        print(f"Your final ticket price is ${ticket_price}.")
else:
    if age <= 5:
        print("Sorry, you are too young to ride the rollercoaster.")
    else:
        print("Sorry, you are not tall enough to ride the rollercoaster.")
