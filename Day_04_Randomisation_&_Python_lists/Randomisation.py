import random

# https://docs.python.org/3/library/random.html
# Documentation for the random module

random_integer = random.randint(
    1, 10
)  # Generates a random integer between 1 and 10 (inclusive)

random_float = random.random()  # Generates a random float between 0.0 and 1.0
random_uniform = random.uniform(
    1.0, 10.0
)  # Generates a random float between 1.0 and 10.0

print(f"Random Integer: {random_integer}")
print(f"Random Float: {random_float}")
print(f"Random Uniform: {random_uniform}")
