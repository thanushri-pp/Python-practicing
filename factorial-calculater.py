def factorial(n):
    """Return factorial of n using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
print("Factorial Calculator")
num = int(input("Enter a number: "))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
