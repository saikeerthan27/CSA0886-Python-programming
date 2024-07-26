def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    gcd_len = gcd(len(str1), len(str2))
    return str1[:gcd_len]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test Case 1
str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))  

# Test Case 2
str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))  
