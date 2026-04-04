# We usually use lists to store multiple items in a single variable which are realted to eachother
# eg countries, fruits, vegetables in a list.
# Lists are created using square brackets [] and items are separated by commas.
# https://docs.python.org/3/tutorial/datastructures.html


fruits = ["apple", "banana", "cherry"]
print(fruits)

# lets change the value of the first item in the list to "orange"

fruits[0] = "orange"
print(fruits)

# We can also add items to the list using the append() method
fruits.append("grape")
print(fruits)

# we can also extend the list using the extend() method
fruits.extend(["kiwi", "mango"])
print(fruits)

# We can also insert an item at a specific position using the insert() method
fruits.insert(1, "strawberry")
print(fruits)

# We can also remove an item from the list using the remove() method
fruits.remove("banana")
print(fruits)

# We can also pop an item from the list using the pop() method
fruits.pop(2)
print(fruits)

# We can also clear the list using the clear() method
fruits.clear()
print(fruits)


# Nested Lists
# A list can also contain other lists, which are called nested lists.
# For example, we can have a list of lists to store the names of fruits and vegetables.
fruits_and_vegetables = [
    ["apple", "banana", "cherry"],
    ["carrot", "broccoli", "spinach"],
]
print(f"fruits_and_vegetables: {fruits_and_vegetables}")
print(f"First fruit: {fruits_and_vegetables[0][0]}")
print(f"First vegetable: {fruits_and_vegetables[1][0]}")
