def convertToBase7(num):
    if num == 0:
        return "0"
    
    is_negative = num < 0
    num = abs(num)
    base7 = []
    
    while num > 0:
        base7.append(str(num % 7))
        num //= 7
    
    if is_negative:
        base7.append('-')
    
    return ''.join(base7[::-1])

# Example usage
input_num = 100
print(convertToBase7(input_num)) 
