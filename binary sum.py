def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Test Case
a = "11"
b = "1"
result = add_binary(a, b)
print(result)
