def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test Case 1
n = 2
print(fibonacci(n))  
# Test Case 2
n = 3
print(fibonacci(n))  
