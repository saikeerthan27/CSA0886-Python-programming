def divide(dividend, divisor):
    if dividend == 0:
        return 0
    negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    if negative:
        quotient = -quotient
    return min(max(-2**31, quotient), 2**31 - 1)
print(divide(10, 3))  
