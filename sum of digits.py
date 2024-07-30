# Input from user
num = int(input("Enter an integer number: "))

# Initialize sum
sum = 0

# Find the sum of digits
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

# Output the sum of digits
print("Sum of the digits:", sum)
