def divide(dividend, divisor):
    # Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Work with absolute values
    dividend, divisor = abs(dividend), abs(divisor)

    # Initialize quotient and temporary value
    quotient = 0
    temp = 0

    # Perform bitwise division
    for i in range(31, -1, -1):  # Check from the highest bit to the lowest
        if temp + (divisor << i) <= dividend:
            temp += divisor << i  # Add the shifted divisor to temp
            quotient |= 1 << i   # Set the corresponding bit in the quotient

    # Apply the sign to the quotient
    return -quotient if sign == -1 else quotient

# Take inputs
a = int(input("Enter dividend (a): "))
b = int(input("Enter divisor (b): "))

# Print the result
print("Result of", a, "/", b, "is", divide(a, b))
