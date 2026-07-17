# we use loops to repeat a block of code multiple times
# there are two types of loops in python: for loops and while loops
# for loops are used to iterate over a sequence (like a list, tuple, or string)
# while loops are used to repeat a block of code as long as a condition is true

fruits = ["apple", "banana", "cherry"]

print("Using a for loop to iterate over the list of fruits:")
# for loop example
for fruit in fruits:
    print(fruit)

print("\nUsing a while loop to print numbers from 0 to 4:")
# while loop example
count = 0
while count < 5:
    print(count)
    count += 1

print("\nUsing a for loop with range() to print numbers from 0 to 4:")
# we can also use the range() function to generate a sequence of numbers
# for example, to print numbers from 0 to 4:
for i in range(5):
    print(i)

print("\nUsing a for loop with range() to print numbers from 1 to 5:")
# we can also specify a start and end point for the range
for i in range(0, 6):
    print(i)


# list to store the highest score
student_scores = [
    85,
    98,
    99,
    70,
    65,
    90,
    98,
    85,
    85,
    84,
    83,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
]

# adding all the stored numbers in list by using sum() function
print(sum(student_scores))

# We can also use for loop to add all the numbers in the list
total = 0
for i in student_scores:
    total += i
print(total)

# Gauss Challange
# Add up numbers from 1 to 100
total = 0
print("\nUsing a for loop with range() to add up numbers from 1 to 100:")
for i in range(1, 101):
    total += i
print(total)

