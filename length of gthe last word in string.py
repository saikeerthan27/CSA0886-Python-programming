def length_of_last_word(s):
    words = s.split()
    if len(words) == 0:
        return 0
    return len(words[-1])

# Test Case
s = "Hello World"
output = length_of_last_word(s)
print(output)
