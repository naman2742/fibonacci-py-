# Function to calculate the nth Fibonacci number
def fibonacci(n):
    # Handling the base cases
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0  # Fibonacci number at position 1
    elif n == 2:
        return 1  # Fibonacci number at position 2
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    return b

# Take input from the user
n = int(input("Enter the position n to find the nth Fibonacci number: "))

# Call the fibonacci function and print the result
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
