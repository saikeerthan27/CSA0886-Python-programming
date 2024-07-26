def addDigits(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

# Test Case 1
num1 = 38
print(addDigits(num1))  

# Test Case 2
num2 = 0
print(addDigits(num2)) 