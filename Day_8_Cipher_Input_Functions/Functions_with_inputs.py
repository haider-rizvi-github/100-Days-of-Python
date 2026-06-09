# Normally, when we create a function, we can only use it to perform a specific task.
#  However, sometimes we want to create a function that can perform a task with different inputs. This is where parameters come in.


def greet():
    print("Hello, World!")
    print("Welcome to learning about functions with inputs.")


greet()


def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How are you {name}?")
    print("Welcome to learning about functions with inputs.")


greet_with_name("Alice")

# Fuctions with more than 1 input


def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")
    print("Welcome to learning about functions with inputs.")


greet_with(location="New York", name="Bob")
