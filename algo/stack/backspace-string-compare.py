class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
        """
        stack1, stack2 = collections.deque(), collections.deque()
        for s in S.split():
            if s != '#':
                stack1.append(s)
            elif stack1:
                stack1.pop()
                
        for t in T.split():
            if t != '#':
                stack2.append(s)
            elif stack2:
                stack2.pop()
                
        return ''.join(stack1) == ''.join(stack2)
        """
"""
844. Backspace String Compare
Easy

884

55

Favorite

Share
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
Accepted
85,889
Submissions
183,518
"""
