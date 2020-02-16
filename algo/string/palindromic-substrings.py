class Solution:
    def countSubstrings(self, S: str) -> int:
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = int(center / 2)
            right = int(left + center % 2)
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

"""
647. Palindromic Substrings
Medium

1971

96

Add to List

Share
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

input = "abc"
output = 3
center, left, right, ans
0 0 0 0
1 0 1 1
2 1 1 1
3 1 2 2
4 2 2 2


"""