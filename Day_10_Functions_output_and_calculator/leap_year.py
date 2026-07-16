def is_leap_year(year):
    """Determines if a given year is a leap year.
    Steps: Use the function and give the year as an argument to the function."""

    # Write your code here.
    first = year % 4 == 0
    second = year % 100 == 0
    third = year % 400 == 0

    # print(bool(first), bool(second), bool(third))

    if first and second and third == True:
        return f"{year} is a leap year."
    elif third == False:
        return f"{year} is not a leap year."



print(is_leap_year(2400))
