class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        print("n: " + str(n))
        def generate(A = []):
            if len(A) == 2 * n:
                if valid(A):
                    print("A is valid")
                    ans.append("".join(A))
                    print("A: " + str(A))
            else:
                A.append('(')
                generate(A)
                print("A: " + str(A))
                A.pop()
                A.append(')')
                generate(A)
                print("A: " + str(A))
                A.pop()
            print("A: " + str(A))
                    
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        
        ans = []
        
        generate()
        
        return ans
        
    def generateParenthesis2(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
    
print(Solution().generateParenthesis2(3))

"""
22. Generate Parentheses
Medium

3502

206

Favorite

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
