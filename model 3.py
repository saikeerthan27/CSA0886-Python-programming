def is_power_of_four(n):
    if n > 0 and (n & (n - 1)) == 0:
        count = 0
        while n > 1:
            n >>= 1
            count += 1
        return count % 2 == 0
    return False

# Test cases
print(is_power_of_four(16)) 
print(is_power_of_four(5))

