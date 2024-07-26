def generateParenthesis(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    res = []
    backtrack('', 0, 0)
    return res
print(generateParenthesis(3))
