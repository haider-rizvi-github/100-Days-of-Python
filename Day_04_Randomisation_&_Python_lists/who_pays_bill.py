import random

print("Welcome to the bill splitter!")

# Variables and data types
TotalNumberOfPeople = input("Enter the numbers of people who will split the bill:")
PeopleList = []


TotalNumberOfPeople = int(TotalNumberOfPeople)  # converting the input to an integer

print(type(TotalNumberOfPeople))  # checking the type of the variable

for i in range(TotalNumberOfPeople):
    name = input("Enter the name of the person: ")
    PeopleList.append(name)

print(PeopleList)

# using random.choice() to select a random name from the list of people
print(f"The person who will pay the bill is: {random.choice(PeopleList)}")
print(
    r"""
     _       _ _            
    | |     | | |           
  __| | ___ | | | __ _ _ __ 
 / _` |/ _ \| | |/ _` | '__|
| (_| | (_) | | | (_| | |   
 \__,_|\___/|_|_|\__,_|_|   
 """
)
