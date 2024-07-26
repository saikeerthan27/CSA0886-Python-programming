def convertToBase7(num):
    if num == 0:
        return "0"
    neg = num < 0
    num = abs(num)
    res = ""
    while num:
        res = str(num % 7) + res
        num //= 7
    return "-" + res if neg else res
print(convertToBase7(100))  
print(convertToBase7(-7))   
