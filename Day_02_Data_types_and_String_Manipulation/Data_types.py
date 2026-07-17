my_number = "+25448548776"
print(my_number[2:5])  # it defines the range of characters.

# We can also use negative indexing to access characters from the end of the string.
print(my_number[-4:])  # it will print the last 4 characters of the string
print(my_number[:-4])  # it will print the string except the last 4 characters

# String
print(
    f"String: {'123' + '456'}"
)  # it will concatenate the two strings together, resulting in "123456"

# Integer
print(f"Integer: {123 + 456}")  # it will add the two numbers together

# Float
print(f"Float: {3.14 + 2.71}")  # it will add the two numbers together

# len(123465) # it will give an error because len() function is used to get the length of a string, list, or other iterable, but not for integers.
print(len("123465"))  # it will return the length of the string, which is 6
print(
    len(str(123465))
)  # it will return the length of the string representation of the integer, which is 6

# You can also check the data type of a variable using the type() function.
print(type(my_number))  # it will return <class 'str'> because my_number is a string
print(type(123))  # it will return <class 'int'> because 123 is an integer
print(type(3.14))  # it will return <class 'float'> because 3.14 is a float
print(type(True))  # it will return <class 'bool'> because True is a boolean value
print(
    type(45645452132156489784531321546546546)
)  # it will return <class 'int'> because it is a very large integer

# Converting between data types
# You can convert between data types using the built-in functions like int(), float(), str(), and bool().
print(int("123"))  # it will convert the string "123" to the integer 123
print(float("3.14"))  # it will convert the string "3.14" to the float 3.14
print(str(123))  # it will convert the integer 123 to the string "123"
print(bool(0))  # it will convert the integer 0 to the boolean value False
print(bool(1))  # it will   convert the integer 1 to the boolean value True
print(bool(""))  # it will convert the empty string "" to the boolean value False
print(
    bool("Hello")
)  # it will convert the non-empty string "Hello" to the boolean value True

# We can see it by printing a length of the input word we type:
print(
    "Number of letters in your name: " + str(len(input("What is your name?")))
)  # it will ask the user for their name and then print the number of letters in their name
