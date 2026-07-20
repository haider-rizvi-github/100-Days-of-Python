"""
We will learn about global and local variables in this file.


"""

enemies = 1  # This is a global variable


# not changing the global variable, just creating a local variable with the same name


def increase_enemies1():
    enemies = 3  # This is a local variable
    print(f"enemies inside function: {enemies}")


# changing the global variable inside the function
def increase_enemies():
    global enemies  # allow us to modify the global variable inside the function
    enemies += 1  # This is a local variable
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

increase_enemies1()
