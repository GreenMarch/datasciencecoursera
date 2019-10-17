class Solution:
    def isValid(self, s):
        stack = []
        bracket_hash = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for item in s:
            if item in bracket_hash:
                stack.append(bracket_hash[item])
            elif not stack or stack.pop() != item:
                return False
        return len(stack) == 0
