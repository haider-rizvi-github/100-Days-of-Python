def addition(num1, num2):
    result = num1 + num2
    return result


print(f"addition(5, 3): {addition(5, 3)}")
print(f"addition(10, 20): {addition(10, 20)}")


def format_name(f_name, l_name):
    fullname = f_name.title() + " " + l_name.title()
    return fullname


print(f"format_name('john', 'doe'): {format_name('john', 'doe')}")

print(f"format_name('jane', 'smith'): {format_name('jane', 'smith')}")


# Multiple return values (We can return multiple values from a function
#  by returning them as a tuple)


def Name_addition(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    full_name = f_name.title() + " " + l_name.title()
    return full_name


print(
    Name_addition(input("What is your first name? "), input("What is your last name? "))
)
