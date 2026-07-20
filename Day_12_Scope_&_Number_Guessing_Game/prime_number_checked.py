def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print("Welcome to the Prime Number Checker!")

number = int(input("Enter a number: "))
print(f"{number} is prime: {is_prime(number)}")
