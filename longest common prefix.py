def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the prefix as the first string
    prefix = strs[0]
    
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            # Shorten the prefix by one character
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test Case 1
strs = ["flower", "flow", "flight"]
output = longestCommonPrefix(strs)
print(output)  # Output: "fl"




                    