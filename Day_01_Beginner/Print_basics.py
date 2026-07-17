# Write your code below this line 👇

# We will learn everything from scratch - the very basics of programming. We will start with printing something on the screen. In Python, we can use the print() function to display text or other information.

print("Hello world!")  # allows you to write a message in console.
print(" ")

# Task:Write a program that uses print statements to print the following recipe into the Output console.
# The text to print is already there, you just need to make it into code.
#  Your code should print all five lines exactly the same as the example output below.
#  Make sure that you don't change any of these existing text as everything, punctuation and casing all need to match!
# Recipe: 1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
#        2. Knead the dough for 10 minutes.
#        3. Add 3g of Salt.
#        4. Leave to rise for 2 hours.
#        5. Bake at 200 degrees C for 30 minutes.

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
print("")

# We can also concatenate the strings using the + operator.
print("Hello" + " " + "coder")

print("")

# allows you to take input from the user. The input will be stored as a string.

# You can write it like this, but to store the input you can use variables.
#  print("Hello" + " " + input("what is your name? ") + "!")

# Create a variable to store the input.
Name = input("what is your name? ")  # Feel free to type your name
print("Hello, " + Name + "!")

# lets check the length of variable Name using the len() function.
print("The length of your name is: " + str(len(Name)))  # we need
