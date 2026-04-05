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

# We can use the max() function to find the highest score in the list
print(max(student_scores))

max = 0
# Lets try it with a for loop
for i in student_scores:
    if i > max:
        max = i
print(max)
