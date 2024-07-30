class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
        
# Test Case
x = 121
sol = Solution()
print(sol.isPalindrome(x))  # Output: true