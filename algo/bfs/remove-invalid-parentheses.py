class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s == "":
            return [""]
        
        BFSQueue, result = [s], []
        visited = set()
        visited.add(s)
        
        def isValid(paren):
            parenCount = 0
            for p in paren:
                if p == '(':
                    parenCount += 1
                elif p == ')':
                    parenCount -= 1
                if parenCount < 0:
                    return False
            return parenCount == 0
        
        minFound = False 
        
        while BFSQueue:
            s = BFSQueue.pop(0) 
            
            if isValid(s):
                result.append(s)
                minFound = True        
            
			#Once a valid expression is found, no need to do any further removals. 
			#Just check for whatever is remaining in the queue
            if minFound:
                continue
            
            for i in range(len(s)):
				#if the chr isn't a parenthisis, don't bother removing it, just continue.
                if s[i] != '(' and s[i] != ')':
                    continue
				#Remove one character after another and add it in the queue, if it wasn't already explored.
                nxt = s[:i] + s[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    BFSQueue.append(nxt)
        
        if result == []:
            return [""]
        
        return result
                
"""
301. Remove Invalid Parentheses
Hard

1863

77

Favorite

Share
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
